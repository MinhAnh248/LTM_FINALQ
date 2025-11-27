from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from models import db, NguoiDung
from api_routes import api
from routes import auth_bp, transaction_bp, category_bp, user_bp, stats_bp
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///expense.db')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
jwt = JWTManager(app)

# Middleware kiểm tra tài khoản bị khóa
@app.before_request
def check_user_status():
    if request.endpoint and 'auth' not in request.endpoint:
        try:
            verify_jwt_in_request(optional=True)
            user_id = get_jwt_identity()
            if user_id:
                user = NguoiDung.query.get(user_id)
                if user and user.trang_thai == 'Bị khóa':
                    return jsonify({'message': 'Tài khoản đã bị khóa'}), 403
        except:
            pass

# Decorator phân quyền admin
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = NguoiDung.query.get(user_id)
        if not user or user.vai_tro_id != 1:
            return jsonify({'message': 'Không có quyền truy cập'}), 403
        return f(*args, **kwargs)
    return decorated

app.register_blueprint(auth_bp)
app.register_blueprint(transaction_bp)
app.register_blueprint(category_bp)
app.register_blueprint(user_bp)
app.register_blueprint(stats_bp)
app.register_blueprint(api)

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message': 'API endpoint không tồn tại'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'message': 'Lỗi server'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
