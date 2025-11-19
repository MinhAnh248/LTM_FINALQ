from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
from models import db, NguoiDung, DanhMuc, GiaoDich, TichLuy, VayNo, ThanhToan, LichSuTichLuy, PhuongPhap
from sqlalchemy import func, extract

api = Blueprint('api', __name__, url_prefix='/api')

# Vay nợ routes
@api.route('/vay-no', methods=['GET'])
@jwt_required()
def get_vay_no():
    user_id = get_jwt_identity()
    vay_nos = VayNo.query.filter_by(nguoi_dung_id=user_id).all()
    return jsonify([{
        'id': v.id, 'ho_ten_vay_no': v.ho_ten_vay_no, 'loai': v.loai,
        'so_tien': v.so_tien, 'lai_suat': v.lai_suat, 'trang_thai': v.trang_thai,
        'ngay_vay_no': v.ngay_vay_no.isoformat(), 'han_tra': v.han_tra.isoformat() if v.han_tra else None
    } for v in vay_nos]), 200

@api.route('/vay-no', methods=['POST'])
@jwt_required()
def create_vay_no():
    user_id = get_jwt_identity()
    data = request.get_json()
    vay_no = VayNo(
        nguoi_dung_id=user_id, ho_ten_vay_no=data['ho_ten_vay_no'],
        loai=data['loai'], so_tien=data['so_tien'], lai_suat=data.get('lai_suat', 0),
        han_tra=datetime.fromisoformat(data['han_tra']) if data.get('han_tra') else None,
        mo_ta=data.get('mo_ta', '')
    )
    db.session.add(vay_no)
    db.session.commit()
    return jsonify({'message': 'Tạo thành công', 'id': vay_no.id}), 201

# Tích lũy routes
@api.route('/tich-luy', methods=['GET'])
@jwt_required()
def get_tich_luy():
    user_id = get_jwt_identity()
    tich_luys = TichLuy.query.filter_by(nguoi_dung_id=user_id).all()
    return jsonify([{
        'id': t.id, 'ten_tich_luy': t.ten_tich_luy,
        'so_tien_muc_tieu': t.so_tien_muc_tieu, 'trang_thai': t.trang_thai,
        'ngay_ket_thuc': t.ngay_ket_thuc.isoformat() if t.ngay_ket_thuc else None
    } for t in tich_luys]), 200

@api.route('/tich-luy', methods=['POST'])
@jwt_required()
def create_tich_luy():
    user_id = get_jwt_identity()
    data = request.get_json()
    tich_luy = TichLuy(
        nguoi_dung_id=user_id, ten_tich_luy=data['ten_tich_luy'],
        so_tien_muc_tieu=data['so_tien_muc_tieu'],
        ngay_ket_thuc=datetime.fromisoformat(data['ngay_ket_thuc']) if data.get('ngay_ket_thuc') else None
    )
    db.session.add(tich_luy)
    db.session.commit()
    return jsonify({'message': 'Tạo thành công', 'id': tich_luy.id}), 201

# Phương pháp routes
@api.route('/phuong-phap', methods=['GET'])
@jwt_required()
def get_phuong_phap():
    phuong_phaps = PhuongPhap.query.all()
    return jsonify([{
        'id': p.id, 'ten_phuong_phap': p.ten_phuong_phap, 'mo_ta': p.mo_ta
    } for p in phuong_phaps]), 200

@api.route('/thanh-toan', methods=['POST'])
@jwt_required()
def create_thanh_toan():
    data = request.get_json()
    thanh_toan = ThanhToan(
        vay_no_id=data['vay_no_id'], so_tien=data['so_tien'], mo_ta=data.get('mo_ta', '')
    )
    vay_no = VayNo.query.get(data['vay_no_id'])
    tong_da_tra = db.session.query(func.sum(ThanhToan.so_tien)).filter_by(vay_no_id=data['vay_no_id']).scalar() or 0
    if tong_da_tra + data['so_tien'] >= vay_no.so_tien:
        vay_no.trang_thai = 'Đã hoàn thành'
    db.session.add(thanh_toan)
    db.session.commit()
    return jsonify({'message': 'Thanh toán thành công'}), 201

# Giới hạn chi tiêu
@api.route('/gioi-han-chi-tieu', methods=['POST'])
@jwt_required()
def set_gioi_han():
    user_id = get_jwt_identity()
    data = request.get_json()
    danh_muc = DanhMuc.query.filter_by(id=data['danh_muc_id'], nguoi_dung_id=user_id).first()
    if danh_muc:
        danh_muc.gioi_han = data['gioi_han']
        db.session.commit()
        return jsonify({'message': 'Đặt giới hạn thành công'}), 200
    return jsonify({'message': 'Không tìm thấy danh mục'}), 404

# Cảnh báo vượt mức
@api.route('/kiem-tra-gioi-han/<int:danh_muc_id>', methods=['GET'])
@jwt_required()
def check_limit(danh_muc_id):
    user_id = get_jwt_identity()
    danh_muc = DanhMuc.query.filter_by(id=danh_muc_id, nguoi_dung_id=user_id).first()
    if not danh_muc or not hasattr(danh_muc, 'gioi_han'):
        return jsonify({'vuot_muc': False}), 200
    
    now = datetime.utcnow()
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    tong_chi = db.session.query(func.sum(GiaoDich.so_tien)).filter(
        GiaoDich.danh_muc_id == danh_muc_id,
        GiaoDich.ngay >= month_start
    ).scalar() or 0
    
    return jsonify({
        'vuot_muc': tong_chi > danh_muc.gioi_han,
        'tong_chi': tong_chi,
        'gioi_han': danh_muc.gioi_han
    }), 200

# Lịch sử tích lũy
@api.route('/lich-su-tich-luy/<int:tich_luy_id>', methods=['GET'])
@jwt_required()
def get_lich_su_tich_luy(tich_luy_id):
    lich_su = LichSuTichLuy.query.filter_by(tich_luy_id=tich_luy_id).all()
    return jsonify([{
        'id': l.id, 'so_tien': l.so_tien, 'ngay': l.ngay.isoformat(), 'mo_ta': l.mo_ta
    } for l in lich_su]), 200

@api.route('/lich-su-tich-luy', methods=['POST'])
@jwt_required()
def add_lich_su_tich_luy():
    data = request.get_json()
    lich_su = LichSuTichLuy(
        tich_luy_id=data['tich_luy_id'],
        so_tien=data['so_tien'],
        mo_ta=data.get('mo_ta', '')
    )
    db.session.add(lich_su)
    db.session.commit()
    return jsonify({'message': 'Thêm thành công'}), 201

# Thống kê chi tiết
@api.route('/thong-ke-chi-tiet', methods=['GET'])
@jwt_required()
def get_thong_ke_chi_tiet():
    user_id = get_jwt_identity()
    thang = request.args.get('thang', datetime.utcnow().month, type=int)
    nam = request.args.get('nam', datetime.utcnow().year, type=int)
    
    danh_mucs = DanhMuc.query.filter_by(nguoi_dung_id=user_id).all()
    danh_muc_ids = [dm.id for dm in danh_mucs]
    
    giao_dichs = db.session.query(
        DanhMuc.ten_danh_muc,
        DanhMuc.loai_danh_muc,
        func.sum(GiaoDich.so_tien).label('tong')
    ).join(GiaoDich).filter(
        GiaoDich.danh_muc_id.in_(danh_muc_ids),
        extract('month', GiaoDich.ngay) == thang,
        extract('year', GiaoDich.ngay) == nam
    ).group_by(DanhMuc.id).all()
    
    return jsonify([{
        'ten_danh_muc': g[0],
        'loai': g[1],
        'tong': float(g[2])
    } for g in giao_dichs]), 200

# Nhắc nhở thanh toán
@api.route('/nhac-nho', methods=['GET'])
@jwt_required()
def get_nhac_nho():
    user_id = get_jwt_identity()
    now = datetime.utcnow()
    next_week = now + timedelta(days=7)
    
    vay_nos = VayNo.query.filter(
        VayNo.nguoi_dung_id == user_id,
        VayNo.trang_thai == 'Đang trả',
        VayNo.han_tra <= next_week,
        VayNo.han_tra >= now
    ).all()
    
    return jsonify([{
        'id': v.id,
        'ho_ten': v.ho_ten_vay_no,
        'so_tien': v.so_tien,
        'han_tra': v.han_tra.isoformat(),
        'loai': v.loai
    } for v in vay_nos]), 200

# Admin routes
@api.route('/admin/users', methods=['GET'])
@jwt_required()
def get_all_users():
    user_id = get_jwt_identity()
    user = NguoiDung.query.get(user_id)
    if user.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền truy cập'}), 403
    
    users = NguoiDung.query.all()
    return jsonify([{
        'id': u.id, 'ho_ten': u.ho_ten, 'email': u.email,
        'so_du': u.so_du, 'trang_thai': u.trang_thai
    } for u in users]), 200

@api.route('/admin/users/<int:user_id>/lock', methods=['PUT'])
@jwt_required()
def lock_user(user_id):
    admin_id = get_jwt_identity()
    admin = NguoiDung.query.get(admin_id)
    if admin.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền'}), 403
    
    user = NguoiDung.query.get(user_id)
    user.trang_thai = 'Bị khóa'
    db.session.commit()
    return jsonify({'message': 'Đã khóa tài khoản'}), 200

@api.route('/admin/users/<int:user_id>/unlock', methods=['PUT'])
@jwt_required()
def unlock_user(user_id):
    admin_id = get_jwt_identity()
    admin = NguoiDung.query.get(admin_id)
    if admin.vai_tro_id != 1:
        return jsonify({'message': 'Không có quyền'}), 403
    
    user = NguoiDung.query.get(user_id)
    user.trang_thai = 'Hoạt động'
    db.session.commit()
    return jsonify({'message': 'Đã mở khóa'}), 200
