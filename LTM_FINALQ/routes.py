from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import bcrypt
from models import db, NguoiDung, DanhMuc, GiaoDich, TichLuy, VayNo, ThanhToan

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
transaction_bp = Blueprint('transaction', __name__, url_prefix='/api')
category_bp = Blueprint('category', __name__, url_prefix='/api')
user_bp = Blueprint('user', __name__, url_prefix='/api/user')
stats_bp = Blueprint('stats', __name__, url_prefix='/api')

# Auth Routes
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('mat_khau') or not data.get('ho_ten'):
        return jsonify({'message': 'Thiếu thông tin'}), 400
    
    if NguoiDung.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email đã tồn tại'}), 400
    
    hashed_password = bcrypt.hashpw(data['mat_khau'].encode('utf-8'), bcrypt.gensalt())
    
    user = NguoiDung(
        ho_ten=data['ho_ten'],
        email=data['email'],
        mat_khau=hashed_password.decode('utf-8'),
        so_du=data.get('so_du', 0)
    )
    
    db.session.add(user)
    db.session.flush()  # Lấy user.id
    
    # Tạo danh mục mặc định
    default_categories = [
        {'loai': 'Chi tiêu', 'ten': 'Ăn uống', 'icon': '🍔'},
        {'loai': 'Chi tiêu', 'ten': 'Giải trí', 'icon': '🎮'},
        {'loai': 'Chi tiêu', 'ten': 'Mua sắm', 'icon': '🛒'},
        {'loai': 'Chi tiêu', 'ten': 'Di chuyển', 'icon': '🚗'},
        {'loai': 'Thu nhập', 'ten': 'Lương', 'icon': '💰'},
        {'loai': 'Thu nhập', 'ten': 'Thưởng', 'icon': '🎁'},
    ]
    
    for cat in default_categories:
        danh_muc = DanhMuc(
            nguoi_dung_id=user.id,
            loai_danh_muc=cat['loai'],
            ten_danh_muc=cat['ten'],
            icon=cat['icon']
        )
        db.session.add(danh_muc)
    
    db.session.commit()
    
    return jsonify({'message': 'Đăng ký thành công', 'user_id': user.id}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    from flask_jwt_extended import create_access_token
    
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('mat_khau'):
        return jsonify({'message': 'Thiếu email hoặc mật khẩu'}), 400
    
    user = NguoiDung.query.filter_by(email=data['email']).first()
    
    if not user or not bcrypt.checkpw(data['mat_khau'].encode('utf-8'), user.mat_khau.encode('utf-8')):
        return jsonify({'message': 'Email hoặc mật khẩu không đúng'}), 401
    
    if user.trang_thai == 'Bị khóa':
        return jsonify({'message': 'Tài khoản đã bị khóa'}), 403
    
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token, 'user_id': user.id}), 200

# Transaction Routes
@transaction_bp.route('/giao-dich', methods=['POST'])
@jwt_required()
def create_transaction():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    danh_muc = DanhMuc.query.filter_by(id=data['danh_muc_id'], nguoi_dung_id=user_id).first()
    if not danh_muc:
        return jsonify({'message': 'Danh mục không tồn tại'}), 404
    
    giao_dich = GiaoDich(
        danh_muc_id=data['danh_muc_id'],
        so_tien=data['so_tien'],
        mo_ta=data.get('mo_ta', '')
    )
    
    user = NguoiDung.query.get(user_id)
    if danh_muc.loai_danh_muc == 'Chi tiêu':
        user.so_du -= data['so_tien']
    else:
        user.so_du += data['so_tien']
    
    db.session.add(giao_dich)
    db.session.commit()
    
    return jsonify({'message': 'Giao dịch thành công', 'so_du_moi': user.so_du}), 201

@transaction_bp.route('/giao-dich', methods=['GET'])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    danh_mucs = DanhMuc.query.filter_by(nguoi_dung_id=user_id).all()
    danh_muc_ids = [dm.id for dm in danh_mucs]
    
    giao_dichs = GiaoDich.query.filter(GiaoDich.danh_muc_id.in_(danh_muc_ids)).all()
    
    return jsonify([{
        'id': g.id,
        'so_tien': g.so_tien,
        'mo_ta': g.mo_ta,
        'ngay': g.ngay.isoformat()
    } for g in giao_dichs]), 200

# Category Routes
@category_bp.route('/danh-muc', methods=['POST'])
@jwt_required()
def create_category():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    danh_muc = DanhMuc(
        nguoi_dung_id=user_id,
        loai_danh_muc=data['loai_danh_muc'],
        ten_danh_muc=data['ten_danh_muc'],
        mo_ta=data.get('mo_ta', ''),
        icon=data.get('icon', '')
    )
    
    db.session.add(danh_muc)
    db.session.commit()
    
    return jsonify({'message': 'Tạo danh mục thành công', 'id': danh_muc.id}), 201

@category_bp.route('/danh-muc', methods=['GET'])
@jwt_required()
def get_categories():
    user_id = get_jwt_identity()
    danh_mucs = DanhMuc.query.filter_by(nguoi_dung_id=user_id).all()
    
    return jsonify([{
        'id': dm.id,
        'ten_danh_muc': dm.ten_danh_muc,
        'loai_danh_muc': dm.loai_danh_muc,
        'icon': dm.icon
    } for dm in danh_mucs]), 200

# User Routes
@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = NguoiDung.query.get(user_id)
    
    return jsonify({
        'id': user.id,
        'ho_ten': user.ho_ten,
        'email': user.email,
        'so_du': user.so_du,
        'trang_thai': user.trang_thai
    }), 200

@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    user = NguoiDung.query.get(user_id)
    
    if 'ho_ten' in data:
        user.ho_ten = data['ho_ten']
    if 'mat_khau' in data:
        user.mat_khau = bcrypt.hashpw(data['mat_khau'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    db.session.commit()
    return jsonify({'message': 'Cập nhật thành công'}), 200

# Statistics Routes
@stats_bp.route('/thong-ke', methods=['GET'])
@jwt_required()
def get_statistics():
    user_id = get_jwt_identity()
    danh_mucs = DanhMuc.query.filter_by(nguoi_dung_id=user_id).all()
    danh_muc_ids = [dm.id for dm in danh_mucs]
    
    now = datetime.utcnow()
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    chi_tieu = db.session.query(db.func.sum(GiaoDich.so_tien)).filter(
        GiaoDich.danh_muc_id.in_(danh_muc_ids),
        GiaoDich.ngay >= month_start,
        DanhMuc.loai_danh_muc == 'Chi tiêu'
    ).join(DanhMuc).scalar() or 0
    
    thu_nhap = db.session.query(db.func.sum(GiaoDich.so_tien)).filter(
        GiaoDich.danh_muc_id.in_(danh_muc_ids),
        GiaoDich.ngay >= month_start,
        DanhMuc.loai_danh_muc == 'Thu nhập'
    ).join(DanhMuc).scalar() or 0
    
    return jsonify({
        'chi_tieu_thang_nay': chi_tieu,
        'thu_nhap_thang_nay': thu_nhap,
        'so_du': NguoiDung.query.get(user_id).so_du
    }), 200
