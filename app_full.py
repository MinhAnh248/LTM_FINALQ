from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from datetime import datetime, timedelta
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///expense.db')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class VaiTro(db.Model):
    __tablename__ = 'vai_tro'
    id = db.Column(db.Integer, primary_key=True)
    loai_vai_tro = db.Column(db.String(50), nullable=False)
    mo_ta = db.Column(db.String(255))

class NguoiDung(db.Model):
    __tablename__ = 'nguoi_dung'
    id = db.Column(db.Integer, primary_key=True)
    vai_tro_id = db.Column(db.Integer, db.ForeignKey('vai_tro.id'), default=2)
    ho_ten = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mat_khau = db.Column(db.String(255), nullable=False)
    so_du = db.Column(db.Float, default=0)
    trang_thai = db.Column(db.String(20), default='Hoạt động')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DanhMuc(db.Model):
    __tablename__ = 'danh_muc'
    id = db.Column(db.Integer, primary_key=True)
    nguoi_dung_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'), nullable=False)
    loai_danh_muc = db.Column(db.String(20), nullable=False)
    ten_danh_muc = db.Column(db.String(100), nullable=False)
    mo_ta = db.Column(db.String(255))
    icon = db.Column(db.String(50))

class GiaoDich(db.Model):
    __tablename__ = 'giao_dich'
    id = db.Column(db.Integer, primary_key=True)
    danh_muc_id = db.Column(db.Integer, db.ForeignKey('danh_muc.id'), nullable=False)
    so_tien = db.Column(db.Float, nullable=False)
    mo_ta = db.Column(db.String(255))
    ngay = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class GioiHanChiTieu(db.Model):
    __tablename__ = 'gioi_han_chi_tieu'
    id = db.Column(db.Integer, primary_key=True)
    danh_muc_id = db.Column(db.Integer, db.ForeignKey('danh_muc.id'), nullable=False)
    so_tien_gioi_han = db.Column(db.Float, nullable=False)
    thang = db.Column(db.Integer)
    nam = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class TichLuy(db.Model):
    __tablename__ = 'tich_luy'
    id = db.Column(db.Integer, primary_key=True)
    nguoi_dung_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'), nullable=False)
    ten_tich_luy = db.Column(db.String(100), nullable=False)
    so_tien_muc_tieu = db.Column(db.Float, nullable=False)
    so_tien_hien_tai = db.Column(db.Float, default=0)
    ngay_ket_thuc = db.Column(db.DateTime)
    trang_thai = db.Column(db.String(20), default='Đang thực hiện')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class LichSuTichLuy(db.Model):
    __tablename__ = 'lich_su_tich_luy'
    id = db.Column(db.Integer, primary_key=True)
    tich_luy_id = db.Column(db.Integer, db.ForeignKey('tich_luy.id'), nullable=False)
    so_tien = db.Column(db.Float, nullable=False)
    ngay = db.Column(db.DateTime, default=datetime.utcnow)
    mo_ta = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class VayNo(db.Model):
    __tablename__ = 'vay_no'
    id = db.Column(db.Integer, primary_key=True)
    nguoi_dung_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'), nullable=False)
    ho_ten_vay_no = db.Column(db.String(100), nullable=False)
    loai = db.Column(db.String(20), nullable=False)
    trang_thai = db.Column(db.String(20), default='Đang trả')
    so_tien = db.Column(db.Float, nullable=False)
    lai_suat = db.Column(db.Float, default=0)
    ngay_vay_no = db.Column(db.DateTime, default=datetime.utcnow)
    han_tra = db.Column(db.DateTime)
    mo_ta = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ThanhToan(db.Model):
    __tablename__ = 'thanh_toan'
    id = db.Column(db.Integer, primary_key=True)
    vay_no_id = db.Column(db.Integer, db.ForeignKey('vay_no.id'), nullable=False)
    so_tien = db.Column(db.Float, nullable=False)
    mo_ta = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PhuongPhap(db.Model):
    __tablename__ = 'phuong_phap'
    id = db.Column(db.Integer, primary_key=True)
    ten_phuong_phap = db.Column(db.String(100), nullable=False)
    mo_ta = db.Column(db.String(500))
    uu_diem = db.Column(db.String(500))
    nhuoc_diem = db.Column(db.String(500))
    cach_van_dung = db.Column(db.String(500))

# Auth Routes
@app.route('/api/auth/register', methods=['POST'])
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
    db.session.commit()
    
    return jsonify({'message': 'Đăng ký thành công', 'user_id': user.id}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
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
@app.route('/api/giao-dich', methods=['POST'])
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

@app.route('/api/giao-dich', methods=['GET'])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    danh_mucs = DanhMuc.query.filter_by(nguoi_dung_id=user_id).all()
    danh_muc_ids = [dm.id for dm in danh_mucs]
    
    giao_dichs = GiaoDich.query.filter(GiaoDich.danh_muc_id.in_(danh_muc_ids)).order_by(GiaoDich.ngay.desc()).all()
    
    return jsonify([{
        'id': g.id,
        'danh_muc_id': g.danh_muc_id,
        'so_tien': g.so_tien,
        'mo_ta': g.mo_ta,
        'ngay': g.ngay.isoformat()
    } for g in giao_dichs]), 200

@app.route('/api/giao-dich/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_transaction(id):
    user_id = get_jwt_identity()
    giao_dich = GiaoDich.query.get(id)
    
    if not giao_dich:
        return jsonify({'message': 'Giao dịch không tồn tại'}), 404
    
    danh_muc = DanhMuc.query.get(giao_dich.danh_muc_id)
    if danh_muc.nguoi_dung_id != user_id:
        return jsonify({'message': 'Không có quyền'}), 403
    
    user = NguoiDung.query.get(user_id)
    if danh_muc.loai_danh_muc == 'Chi tiêu':
        user.so_du += giao_dich.so_tien
    else:
        user.so_du -= giao_dich.so_tien
    
    db.session.delete(giao_dich)
    db.session.commit()
    
    return jsonify({'message': 'Xóa giao dịch thành công'}), 200

# Category Routes
@app.route('/api/danh-muc', methods=['POST'])
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

@app.route('/api/danh-muc', methods=['GET'])
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

@app.route('/api/danh-muc/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_category(id):
    user_id = get_jwt_identity()
    danh_muc = DanhMuc.query.get(id)
    
    if not danh_muc or danh_muc.nguoi_dung_id != user_id:
        return jsonify({'message': 'Danh mục không tồn tại'}), 404
    
    db.session.delete(danh_muc)
    db.session.commit()
    
    return jsonify({'message': 'Xóa danh mục thành công'}), 200

# Spending Limit Routes
@app.route('/api/gioi-han', methods=['POST'])
@jwt_required()
def set_spending_limit():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    danh_muc = DanhMuc.query.filter_by(id=data['danh_muc_id'], nguoi_dung_id=user_id).first()
    if not danh_muc:
        return jsonify({'message': 'Danh mục không tồn tại'}), 404
    
    now = datetime.utcnow()
    gioi_han = GioiHanChiTieu.query.filter_by(
        danh_muc_id=data['danh_muc_id'],
        thang=now.month,
        nam=now.year
    ).first()
    
    if gioi_han:
        gioi_han.so_tien_gioi_han = data['so_tien_gioi_han']
    else:
        gioi_han = GioiHanChiTieu(
            danh_muc_id=data['danh_muc_id'],
            so_tien_gioi_han=data['so_tien_gioi_han'],
            thang=now.month,
            nam=now.year
        )
        db.session.add(gioi_han)
    
    db.session.commit()
    return jsonify({'message': 'Đặt giới hạn thành công'}), 201

@app.route('/api/gioi-han/<int:danh_muc_id>', methods=['GET'])
@jwt_required()
def get_spending_limit(danh_muc_id):
    user_id = get_jwt_identity()
    danh_muc = DanhMuc.query.filter_by(id=danh_muc_id, nguoi_dung_id=user_id).first()
    
    if not danh_muc:
        return jsonify({'message': 'Danh mục không tồn tại'}), 404
    
    now = datetime.utcnow()
    gioi_han = GioiHanChiTieu.query.filter_by(
        danh_muc_id=danh_muc_id,
        thang=now.month,
        nam=now.year
    ).first()
    
    if not gioi_han:
        return jsonify({'so_tien_gioi_han': 0, 'chi_tieu_hien_tai': 0}), 200
    
    chi_tieu = db.session.query(db.func.sum(GiaoDich.so_tien)).filter(
        GiaoDich.danh_muc_id == danh_muc_id,
        db.extract('month', GiaoDich.ngay) == now.month,
        db.extract('year', GiaoDich.ngay) == now.year
    ).scalar() or 0
    
    return jsonify({
        'so_tien_gioi_han': gioi_han.so_tien_gioi_han,
        'chi_tieu_hien_tai': chi_tieu,
        'vuot_gioi_han': chi_tieu > gioi_han.so_tien_gioi_han
    }), 200

# Savings Routes
@app.route('/api/tich-luy', methods=['POST'])
@jwt_required()
def create_savings():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    tich_luy = TichLuy(
        nguoi_dung_id=user_id,
        ten_tich_luy=data['ten_tich_luy'],
        so_tien_muc_tieu=data['so_tien_muc_tieu'],
        ngay_ket_thuc=datetime.fromisoformat(data['ngay_ket_thuc']) if data.get('ngay_ket_thuc') else None
    )
    
    db.session.add(tich_luy)
    db.session.commit()
    
    return jsonify({'message': 'Tạo mục tiêu tiết kiệm thành công', 'id': tich_luy.id}), 201

@app.route('/api/tich-luy', methods=['GET'])
@jwt_required()
def get_savings():
    user_id = get_jwt_identity()
    tich_luys = TichLuy.query.filter_by(nguoi_dung_id=user_id).all()
    
    return jsonify([{
        'id': tl.id,
        'ten_tich_luy': tl.ten_tich_luy,
        'so_tien_muc_tieu': tl.so_tien_muc_tieu,
        'so_tien_hien_tai': tl.so_tien_hien_tai,
        'trang_thai': tl.trang_thai,
        'tien_do': (tl.so_tien_hien_tai / tl.so_tien_muc_tieu * 100) if tl.so_tien_muc_tieu > 0 else 0
    } for tl in tich_luys]), 200

@app.route('/api/tich-luy/<int:id>/them', methods=['POST'])
@jwt_required()
def add_savings(id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    tich_luy = TichLuy.query.filter_by(id=id, nguoi_dung_id=user_id).first()
    if not tich_luy:
        return jsonify({'message': 'Mục tiêu không tồn tại'}), 404
    
    tich_luy.so_tien_hien_tai += data['so_tien']
    
    if tich_luy.so_tien_hien_tai >= tich_luy.so_tien_muc_tieu:
        tich_luy.trang_thai = 'Hoàn thành'
    
    lich_su = LichSuTichLuy(
        tich_luy_id=id,
        so_tien=data['so_tien'],
        mo_ta=data.get('mo_ta', '')
    )
    
    db.session.add(lich_su)
    db.session.commit()
    
    return jsonify({'message': 'Thêm tiết kiệm thành công'}), 201

# Debt Routes
@app.route('/api/vay-no', methods=['POST'])
@jwt_required()
def create_debt():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    vay_no = VayNo(
        nguoi_dung_id=user_id,
        ho_ten_vay_no=data['ho_ten_vay_no'],
        loai=data['loai'],
        so_tien=data['so_tien'],
        lai_suat=data.get('lai_suat', 0),
        han_tra=datetime.fromisoformat(data['han_tra']) if data.get('han_tra') else None,
        mo_ta=data.get('mo_ta', '')
    )
    
    db.session.add(vay_no)
    db.session.commit()
    
    return jsonify({'message': 'Thêm khoản vay nợ thành công', 'id': vay_no.id}), 201

@app.route('/api/vay-no', methods=['GET'])
@jwt_required()
def get_debts():
    user_id = get_jwt_identity()
    vay_nos = VayNo.query.filter_by(nguoi_dung_id=user_id).all()
    
    return jsonify([{
        'id': vn.id,
        'ho_ten_vay_no': vn.ho_ten_vay_no,
        'loai': vn.loai,
        'so_tien': vn.so_tien,
        'lai_suat': vn.lai_suat,
        'trang_thai': vn.trang_thai,
        'han_tra': vn.han_tra.isoformat() if vn.han_tra else None
    } for vn in vay_nos]), 200

@app.route('/api/vay-no/<int:id>/thanh-toan', methods=['POST'])
@jwt_required()
def pay_debt(id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    vay_no = VayNo.query.filter_by(id=id, nguoi_dung_id=user_id).first()
    if not vay_no:
        return jsonify({'message': 'Khoản vay không tồn tại'}), 404
    
    thanh_toan = ThanhToan(
        vay_no_id=id,
        so_tien=data['so_tien'],
        mo_ta=data.get('mo_ta', '')
    )
    
    db.session.add(thanh_toan)
    db.session.commit()
    
    return jsonify({'message': 'Thanh toán thành công'}), 201

# Methods Routes
@app.route('/api/phuong-phap', methods=['GET'])
def get_methods():
    phuong_phaps = PhuongPhap.query.all()
    
    return jsonify([{
        'id': pp.id,
        'ten_phuong_phap': pp.ten_phuong_phap,
        'mo_ta': pp.mo_ta,
        'uu_diem': pp.uu_diem,
        'nhuoc_diem': pp.nhuoc_diem,
        'cach_van_dung': pp.cach_van_dung
    } for pp in phuong_phaps]), 200

# User Routes
@app.route('/api/user/profile', methods=['GET'])
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

@app.route('/api/user/profile', methods=['PUT'])
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
@app.route('/api/thong-ke', methods=['GET'])
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
    
    tich_luy_total = db.session.query(db.func.sum(TichLuy.so_tien_hien_tai)).filter(
        TichLuy.nguoi_dung_id == user_id
    ).scalar() or 0
    
    vay_no_total = db.session.query(db.func.sum(VayNo.so_tien)).filter(
        VayNo.nguoi_dung_id == user_id,
        VayNo.trang_thai == 'Đang trả'
    ).scalar() or 0
    
    return jsonify({
        'chi_tieu_thang_nay': chi_tieu,
        'thu_nhap_thang_nay': thu_nhap,
        'so_du': NguoiDung.query.get(user_id).so_du,
        'tich_luy_total': tich_luy_total,
        'vay_no_total': vay_no_total
    }), 200

@app.route('/api/thong-ke/chi-tieu-theo-danh-muc', methods=['GET'])
@jwt_required()
def get_expense_by_category():
    user_id = get_jwt_identity()
    danh_mucs = DanhMuc.query.filter_by(nguoi_dung_id=user_id, loai_danh_muc='Chi tiêu').all()
    
    result = []
    for dm in danh_mucs:
        total = db.session.query(db.func.sum(GiaoDich.so_tien)).filter(
            GiaoDich.danh_muc_id == dm.id
        ).scalar() or 0
        result.append({
            'ten_danh_muc': dm.ten_danh_muc,
            'so_tien': total
        })
    
    return jsonify(result), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
