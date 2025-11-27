from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import bcrypt
import os

app = Flask(__name__)
CORS(app)

# Cấu hình database
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "expense.db")}'
print(f"Database path: {os.path.join(basedir, 'instance', 'expense.db')}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models đơn giản
class NguoiDung(db.Model):
    __tablename__ = 'nguoi_dung'
    id = db.Column(db.Integer, primary_key=True)
    vai_tro_id = db.Column(db.Integer, default=2)
    ho_ten = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mat_khau = db.Column(db.String(255), nullable=False)
    so_du = db.Column(db.Float, default=0)
    trang_thai = db.Column(db.String(20), default='Hoạt động')

class GiaoDich(db.Model):
    __tablename__ = 'giao_dich'
    id = db.Column(db.Integer, primary_key=True)

# Admin Login
@app.route('/api/auth/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('mat_khau'):
        return jsonify({'message': 'Thiếu email hoặc mật khẩu'}), 400
    
    user = NguoiDung.query.filter_by(email=data['email']).first()
    
    if not user:
        return jsonify({'message': 'Email không tồn tại'}), 401
    
    try:
        if not bcrypt.checkpw(data['mat_khau'].encode('utf-8'), user.mat_khau.encode('utf-8')):
            return jsonify({'message': 'Mật khẩu không đúng'}), 401
    except:
        return jsonify({'message': 'Lỗi xác thực mật khẩu'}), 401
    
    # Kiểm tra quyền admin
    if user.vai_tro_id != 1:
        return jsonify({'message': 'Bạn không có quyền truy cập admin'}), 403
    
    if user.trang_thai == 'Bị khóa':
        return jsonify({'message': 'Tài khoản đã bị khóa'}), 403
    
    access_token = create_access_token(identity=str(user.id))
    return jsonify({'access_token': access_token, 'user_id': user.id}), 200

# Get all users
@app.route('/api/admin/users', methods=['GET'])
@jwt_required()
def get_all_users():
    try:
        admin_id = int(get_jwt_identity())
        admin = NguoiDung.query.get(admin_id)
        
        if not admin or admin.vai_tro_id != 1:
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
    except Exception as e:
        return jsonify({'message': f'Lỗi: {str(e)}'}), 500

# Lock user
@app.route('/api/admin/users/<int:user_id>/lock', methods=['PUT'])
@jwt_required()
def lock_user(user_id):
    try:
        admin_id = int(get_jwt_identity())
        admin = NguoiDung.query.get(admin_id)
        
        if not admin or admin.vai_tro_id != 1:
            return jsonify({'message': 'Không có quyền'}), 403
        
        user = NguoiDung.query.get(user_id)
        if not user:
            return jsonify({'message': 'Người dùng không tồn tại'}), 404
        
        user.trang_thai = 'Bị khóa'
        db.session.commit()
        return jsonify({'message': 'Đã khóa tài khoản'}), 200
    except Exception as e:
        return jsonify({'message': f'Lỗi: {str(e)}'}), 500

# Unlock user
@app.route('/api/admin/users/<int:user_id>/unlock', methods=['PUT'])
@jwt_required()
def unlock_user(user_id):
    try:
        admin_id = int(get_jwt_identity())
        admin = NguoiDung.query.get(admin_id)
        
        if not admin or admin.vai_tro_id != 1:
            return jsonify({'message': 'Không có quyền'}), 403
        
        user = NguoiDung.query.get(user_id)
        if not user:
            return jsonify({'message': 'Người dùng không tồn tại'}), 404
        
        user.trang_thai = 'Hoạt động'
        db.session.commit()
        return jsonify({'message': 'Đã mở khóa tài khoản'}), 200
    except Exception as e:
        return jsonify({'message': f'Lỗi: {str(e)}'}), 500

if __name__ == '__main__':
    print("🔐 Admin Backend đơn giản chạy trên http://localhost:5111")
    print("📧 Email: admin@admin.com")
    print("🔑 Password: 123456")
    app.run(debug=True, port=5111)