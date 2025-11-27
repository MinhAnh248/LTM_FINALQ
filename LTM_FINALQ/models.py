from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

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
    gioi_han = db.Column(db.Float, default=0)

class GiaoDich(db.Model):
    __tablename__ = 'giao_dich'
    id = db.Column(db.Integer, primary_key=True)
    danh_muc_id = db.Column(db.Integer, db.ForeignKey('danh_muc.id'), nullable=False)
    so_tien = db.Column(db.Float, nullable=False)
    mo_ta = db.Column(db.String(255))
    ngay = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class TichLuy(db.Model):
    __tablename__ = 'tich_luy'
    id = db.Column(db.Integer, primary_key=True)
    nguoi_dung_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'), nullable=False)
    ten_tich_luy = db.Column(db.String(100), nullable=False)
    so_tien_muc_tieu = db.Column(db.Float, nullable=False)
    ngay_ket_thuc = db.Column(db.DateTime)
    trang_thai = db.Column(db.String(20), default='Đang thực hiện')

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
    nguoi_dung_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'), nullable=False)
    ten_phuong_phap = db.Column(db.String(100), nullable=False)
    mo_ta = db.Column(db.String(255))
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
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DanhMucLoaiPhuongPhap(db.Model):
    __tablename__ = 'danh_muc_loai_phuong_phap'
    id = db.Column(db.Integer, primary_key=True)
    ten_loai = db.Column(db.String(100), nullable=False)
    mo_ta = db.Column(db.String(255))

class ThongTinPhuongPhap(db.Model):
    __tablename__ = 'thong_tin_phuong_phap'
    id = db.Column(db.Integer, primary_key=True)
    phuong_phap_id = db.Column(db.Integer, db.ForeignKey('phuong_phap.id'), nullable=False)
    mdlpp_id = db.Column(db.Integer, db.ForeignKey('danh_muc_loai_phuong_phap.id'), nullable=False)
    loai = db.Column(db.String(50), nullable=False)
    mo_ta = db.Column(db.String(500), nullable=False)
