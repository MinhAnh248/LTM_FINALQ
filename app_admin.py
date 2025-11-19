from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS
from datetime import timedelta
import bcrypt
import os
from dotenv import load_dotenv
from models import db, NguoiDung, DanhMuc, GiaoDich, VaiTro

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///instance/expense.db')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)

db.init_app(app)
jwt = JWTManager(app)

# Admin Login
@app.route('/api/auth/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('mat_khau'):
        return jsonify({'message': 'Thiếu email hoặc mật khẩu'}), 400
    
    user = NguoiDung.query.filter_by(email=data['email']).first()
    
    if not user or not bcrypt.checkpw(data['mat_khau'].encode('utf-8'), user.mat_khau.encode('utf-8')):
        return jsonify({'message': 'Email hoặc mật khẩu không đúng'}), 401
    
    # Kiểm tra quyền admin
    if user.vai_tro_id != 1:
        return jsonify({'message': 'Bạn không có quyền truy cập'}), 403
    
    if user.trang_thai == 'Bị khóa':
        return jsonify({'message': 'Tài khoản đã bị khóa'}), 403
    
    access_token = create_access_token(identity=str(user.id))
    return jsonify({'access_token': access_token, 'user_id': user.id}), 200

# Get all users
@app.route('/api/admin/users', methods=['GET'])
@jwt_required()
def get_all_users():
    admin_id = int(get_jwt_identity())
    admin = NguoiDung.query.get(admin_id)
    
    if admin.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền'}), 403
    
    users = NguoiDung.query.all()
    return jsonify([{
        'id': u.id,
        'ho_ten': u.ho_ten,
        'email': u.email,
        'so_du': u.so_du,
        'trang_thai': u.trang_thai,
        'vai_tro_id': u.vai_tro_id
    } for u in users]), 200

# Lock user
@app.route('/api/admin/users/<int:user_id>/lock', methods=['PUT'])
@jwt_required()
def lock_user(user_id):
    admin_id = int(get_jwt_identity())
    admin = NguoiDung.query.get(admin_id)
    
    if admin.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền'}), 403
    
    user = NguoiDung.query.get(user_id)
    if not user:
        return jsonify({'message': 'Người dùng không tồn tại'}), 404
    
    user.trang_thai = 'Bị khóa'
    db.session.commit()
    return jsonify({'message': 'Đã khóa tài khoản'}), 200

# Unlock user
@app.route('/api/admin/users/<int:user_id>/unlock', methods=['PUT'])
@jwt_required()
def unlock_user(user_id):
    admin_id = int(get_jwt_identity())
    admin = NguoiDung.query.get(admin_id)
    
    if admin.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền'}), 403
    
    user = NguoiDung.query.get(user_id)
    if not user:
        return jsonify({'message': 'Người dùng không tồn tại'}), 404
    
    user.trang_thai = 'Hoạt động'
    db.session.commit()
    return jsonify({'message': 'Đã mở khóa tài khoản'}), 200

# Delete user
@app.route('/api/admin/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    admin_id = int(get_jwt_identity())
    admin = NguoiDung.query.get(admin_id)
    
    if admin.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền'}), 403
    
    user = NguoiDung.query.get(user_id)
    if not user:
        return jsonify({'message': 'Người dùng không tồn tại'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Đã xóa người dùng'}), 200

# Get statistics
@app.route('/api/admin/stats', methods=['GET'])
@jwt_required()
def get_admin_stats():
    admin_id = int(get_jwt_identity())
    admin = NguoiDung.query.get(admin_id)
    
    if admin.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền'}), 403
    
    total_users = NguoiDung.query.count()
    active_users = NguoiDung.query.filter_by(trang_thai='Hoạt động').count()
    total_transactions = GiaoDich.query.count()
    
    return jsonify({
        'total_users': total_users,
        'active_users': active_users,
        'total_transactions': total_transactions
    }), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("🔐 Admin Backend chạy trên http://localhost:5111")
    app.run(debug=True, port=5111)
