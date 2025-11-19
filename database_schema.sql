-- ============================================================================
-- HE THONG QUAN LY CHI TIEU - DATABASE SCHEMA
-- Database: SQLite
-- ORM: SQLAlchemy
-- Total Tables: 10
-- ============================================================================

-- ============================================================================
-- 1. BANG VAI_TRO (Roles)
-- ============================================================================
CREATE TABLE vai_tro (
    id INTEGER NOT NULL PRIMARY KEY,
    loai_vai_tro VARCHAR(50) NOT NULL,  -- 'admin' hoac 'user'
    mo_ta VARCHAR(255)
);

-- Du lieu mau
INSERT INTO vai_tro VALUES (1, 'admin', 'Quan tri vien');
INSERT INTO vai_tro VALUES (2, 'user', 'Nguoi dung');

-- ============================================================================
-- 2. BANG NGUOI_DUNG (Users)
-- ============================================================================
CREATE TABLE nguoi_dung (
    id INTEGER NOT NULL PRIMARY KEY,
    vai_tro_id INTEGER DEFAULT 2,
    ho_ten VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    mat_khau VARCHAR(255) NOT NULL,      -- Bcrypt hashed
    so_du FLOAT DEFAULT 0,
    trang_thai VARCHAR(20) DEFAULT 'Hoat dong',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(vai_tro_id) REFERENCES vai_tro(id)
);

CREATE INDEX idx_nguoi_dung_email ON nguoi_dung(email);
CREATE INDEX idx_nguoi_dung_vai_tro ON nguoi_dung(vai_tro_id);

-- ============================================================================
-- 3. BANG DANH_MUC (Categories)
-- ============================================================================
CREATE TABLE danh_muc (
    id INTEGER NOT NULL PRIMARY KEY,
    nguoi_dung_id INTEGER NOT NULL,
    loai_danh_muc VARCHAR(20) NOT NULL,  -- 'Thu nhap' hoac 'Chi tieu'
    ten_danh_muc VARCHAR(100) NOT NULL,
    mo_ta VARCHAR(255),
    icon VARCHAR(50),
    gioi_han FLOAT DEFAULT 0,            -- Gioi han chi tieu
    FOREIGN KEY(nguoi_dung_id) REFERENCES nguoi_dung(id)
);

CREATE INDEX idx_danh_muc_user ON danh_muc(nguoi_dung_id);
CREATE INDEX idx_danh_muc_loai ON danh_muc(loai_danh_muc);

-- Du lieu mau
INSERT INTO danh_muc VALUES (1, 1, 'Chi tieu', 'An uong', 'An uong hang ngay', '🍔', 5000000);
INSERT INTO danh_muc VALUES (2, 1, 'Chi tieu', 'Giai tri', 'Vui choi', '🎮', 2000000);
INSERT INTO danh_muc VALUES (3, 1, 'Thu nhap', 'Luong', 'Luong thang', '💰', 0);

-- ============================================================================
-- 4. BANG GIAO_DICH (Transactions)
-- ============================================================================
CREATE TABLE giao_dich (
    id INTEGER NOT NULL PRIMARY KEY,
    danh_muc_id INTEGER NOT NULL,
    so_tien FLOAT NOT NULL,
    mo_ta VARCHAR(255),
    ngay DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(danh_muc_id) REFERENCES danh_muc(id)
);

CREATE INDEX idx_giao_dich_danh_muc ON giao_dich(danh_muc_id);
CREATE INDEX idx_giao_dich_ngay ON giao_dich(ngay);

-- ============================================================================
-- 5. BANG TICH_LUY (Savings Goals)
-- ============================================================================
CREATE TABLE tich_luy (
    id INTEGER NOT NULL PRIMARY KEY,
    nguoi_dung_id INTEGER NOT NULL,
    ten_tich_luy VARCHAR(100) NOT NULL,
    so_tien_muc_tieu FLOAT NOT NULL,
    ngay_ket_thuc DATETIME,
    trang_thai VARCHAR(20) DEFAULT 'Dang thuc hien',
    FOREIGN KEY(nguoi_dung_id) REFERENCES nguoi_dung(id)
);

CREATE INDEX idx_tich_luy_user ON tich_luy(nguoi_dung_id);

-- ============================================================================
-- 6. BANG LICH_SU_TICH_LUY (Savings History)
-- ============================================================================
CREATE TABLE lich_su_tich_luy (
    id INTEGER NOT NULL PRIMARY KEY,
    tich_luy_id INTEGER NOT NULL,
    so_tien FLOAT NOT NULL,
    ngay DATETIME DEFAULT CURRENT_TIMESTAMP,
    mo_ta VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(tich_luy_id) REFERENCES tich_luy(id)
);

CREATE INDEX idx_lich_su_tich_luy ON lich_su_tich_luy(tich_luy_id);

-- ============================================================================
-- 7. BANG VAY_NO (Loans/Debts)
-- ============================================================================
CREATE TABLE vay_no (
    id INTEGER NOT NULL PRIMARY KEY,
    nguoi_dung_id INTEGER NOT NULL,
    ho_ten_vay_no VARCHAR(100) NOT NULL,
    loai VARCHAR(20) NOT NULL,           -- 'Cho Vay' hoac 'Muon No'
    trang_thai VARCHAR(20) DEFAULT 'Dang tra',
    so_tien FLOAT NOT NULL,
    lai_suat FLOAT DEFAULT 0,
    ngay_vay_no DATETIME DEFAULT CURRENT_TIMESTAMP,
    han_tra DATETIME,
    mo_ta VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(nguoi_dung_id) REFERENCES nguoi_dung(id)
);

CREATE INDEX idx_vay_no_user ON vay_no(nguoi_dung_id);
CREATE INDEX idx_vay_no_trang_thai ON vay_no(trang_thai);

-- ============================================================================
-- 8. BANG THANH_TOAN (Payments)
-- ============================================================================
CREATE TABLE thanh_toan (
    id INTEGER NOT NULL PRIMARY KEY,
    vay_no_id INTEGER NOT NULL,
    so_tien FLOAT NOT NULL,
    mo_ta VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(vay_no_id) REFERENCES vay_no(id)
);

CREATE INDEX idx_thanh_toan_vay_no ON thanh_toan(vay_no_id);

-- ============================================================================
-- 9. BANG PHUONG_PHAP (Methods)
-- ============================================================================
CREATE TABLE phuong_phap (
    id INTEGER NOT NULL PRIMARY KEY,
    nguoi_dung_id INTEGER NOT NULL,
    ten_phuong_phap VARCHAR(100) NOT NULL,
    mo_ta VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(nguoi_dung_id) REFERENCES nguoi_dung(id)
);

-- ============================================================================
-- 10. BANG DANH_MUC_LOAI_PHUONG_PHAP (Method Categories)
-- ============================================================================
CREATE TABLE danh_muc_loai_phuong_phap (
    id INTEGER NOT NULL PRIMARY KEY,
    ten_loai VARCHAR(100) NOT NULL,
    mo_ta VARCHAR(255)
);

-- ============================================================================
-- 11. BANG THONG_TIN_PHUONG_PHAP (Method Details)
-- ============================================================================
CREATE TABLE thong_tin_phuong_phap (
    id INTEGER NOT NULL PRIMARY KEY,
    phuong_phap_id INTEGER NOT NULL,
    mdlpp_id INTEGER NOT NULL,
    loai VARCHAR(50) NOT NULL,
    mo_ta VARCHAR(500) NOT NULL,
    FOREIGN KEY(phuong_phap_id) REFERENCES phuong_phap(id),
    FOREIGN KEY(mdlpp_id) REFERENCES danh_muc_loai_phuong_phap(id)
);

-- ============================================================================
-- RELATIONSHIPS (ERD)
-- ============================================================================
-- VaiTro (1) ----< (N) NguoiDung
-- NguoiDung (1) ----< (N) DanhMuc
-- NguoiDung (1) ----< (N) TichLuy
-- NguoiDung (1) ----< (N) VayNo
-- NguoiDung (1) ----< (N) PhuongPhap
-- DanhMuc (1) ----< (N) GiaoDich
-- TichLuy (1) ----< (N) LichSuTichLuy
-- VayNo (1) ----< (N) ThanhToan
-- PhuongPhap (1) ----< (N) ThongTinPhuongPhap
-- DanhMucLoaiPhuongPhap (1) ----< (N) ThongTinPhuongPhap

-- ============================================================================
-- USEFUL QUERIES
-- ============================================================================

-- Thong ke chi tieu theo thang
SELECT 
    dm.ten_danh_muc,
    SUM(gd.so_tien) as tong_chi
FROM giao_dich gd
JOIN danh_muc dm ON gd.danh_muc_id = dm.id
WHERE dm.nguoi_dung_id = ? 
    AND dm.loai_danh_muc = 'Chi tieu'
    AND strftime('%m', gd.ngay) = ?
    AND strftime('%Y', gd.ngay) = ?
GROUP BY dm.id;

-- Kiem tra vuot gioi han
SELECT 
    dm.ten_danh_muc,
    dm.gioi_han,
    SUM(gd.so_tien) as tong_chi
FROM giao_dich gd
JOIN danh_muc dm ON gd.danh_muc_id = dm.id
WHERE dm.nguoi_dung_id = ?
    AND dm.loai_danh_muc = 'Chi tieu'
    AND strftime('%m', gd.ngay) = strftime('%m', 'now')
GROUP BY dm.id
HAVING SUM(gd.so_tien) > dm.gioi_han;

-- Nhac nho thanh toan (7 ngay toi)
SELECT * FROM vay_no
WHERE nguoi_dung_id = ?
    AND trang_thai = 'Dang tra'
    AND han_tra BETWEEN datetime('now') AND datetime('now', '+7 days');

-- Tong thu nhap va chi tieu
SELECT 
    dm.loai_danh_muc,
    SUM(gd.so_tien) as tong
FROM giao_dich gd
JOIN danh_muc dm ON gd.danh_muc_id = dm.id
WHERE dm.nguoi_dung_id = ?
GROUP BY dm.loai_danh_muc;
