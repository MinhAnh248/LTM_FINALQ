# KIẾN TRÚC ĐA NGƯỜI DÙNG (MULTI-USER)

## ✅ Hệ thống hỗ trợ NHIỀU NGƯỜI DÙNG độc lập

### 1. Cơ chế phân tách dữ liệu

```
┌─────────────────────────────────────────────────────────┐
│                    DATABASE CHUNG                        │
├─────────────────────────────────────────────────────────┤
│  User A                User B                User C      │
│  ├─ DanhMuc A1        ├─ DanhMuc B1        ├─ DanhMuc C1│
│  ├─ GiaoDich A1       ├─ GiaoDich B1       ├─ GiaoDich C1│
│  ├─ TichLuy A1        ├─ TichLuy B1        ├─ TichLuy C1│
│  └─ VayNo A1          └─ VayNo B1          └─ VayNo C1  │
└─────────────────────────────────────────────────────────┘
```

### 2. Bảng NguoiDung - Trung tâm phân quyền

```sql
CREATE TABLE nguoi_dung (
    id INTEGER PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,  -- Mỗi user 1 email riêng
    mat_khau VARCHAR(255) NOT NULL,      -- Mật khẩu riêng
    vai_tro_id INTEGER DEFAULT 2,        -- Role: admin/user
    so_du FLOAT DEFAULT 0,               -- Số dư riêng
    trang_thai VARCHAR(20)               -- Trạng thái riêng
);
```

**Đặc điểm:**
- ✅ Email UNIQUE → Mỗi người 1 tài khoản
- ✅ Mật khẩu hash riêng (bcrypt)
- ✅ Số dư tài chính riêng biệt
- ✅ Trạng thái độc lập (Hoạt động/Bị khóa)

### 3. Dữ liệu được phân tách theo nguoi_dung_id

#### 3.1. Bảng DanhMuc (Categories)
```sql
CREATE TABLE danh_muc (
    id INTEGER PRIMARY KEY,
    nguoi_dung_id INTEGER NOT NULL,  -- ← Khóa phân tách
    ten_danh_muc VARCHAR(100),
    FOREIGN KEY(nguoi_dung_id) REFERENCES nguoi_dung(id)
);
```

**Ví dụ thực tế:**
```
User A (id=1):
  - Danh mục: "Ăn uống", "Giải trí", "Lương"
  
User B (id=2):
  - Danh mục: "Mua sắm", "Du lịch", "Thưởng"
  
User C (id=3):
  - Danh mục: "Học phí", "Sách vở", "Part-time"
```

#### 3.2. Bảng GiaoDich (Transactions)
```sql
-- Giao dịch thuộc về danh mục
-- Danh mục thuộc về người dùng
-- → Giao dịch gián tiếp thuộc về người dùng

GiaoDich → danh_muc_id → DanhMuc → nguoi_dung_id → NguoiDung
```

**Cách truy vấn:**
```sql
-- Chỉ lấy giao dịch của User A (id=1)
SELECT gd.* 
FROM giao_dich gd
JOIN danh_muc dm ON gd.danh_muc_id = dm.id
WHERE dm.nguoi_dung_id = 1;
```

#### 3.3. Các bảng khác
```sql
-- Tích lũy
tich_luy.nguoi_dung_id → Mỗi user có mục tiêu riêng

-- Vay nợ
vay_no.nguoi_dung_id → Mỗi user quản lý nợ riêng

-- Phương pháp
phuong_phap.nguoi_dung_id → Mỗi user có phương pháp riêng
```

### 4. Bảo mật & Phân quyền

#### 4.1. JWT Authentication
```python
# Khi user đăng nhập
token = jwt.encode({
    'user_id': user.id,      # ID người dùng
    'email': user.email,
    'role': user.vai_tro_id
}, SECRET_KEY)
```

#### 4.2. Middleware kiểm tra quyền
```python
@app.route('/api/giao-dich', methods=['GET'])
@token_required
def get_transactions(current_user):
    # current_user.id được lấy từ JWT token
    # Chỉ lấy giao dịch của user hiện tại
    danh_muc = DanhMuc.query.filter_by(
        nguoi_dung_id=current_user.id
    ).all()
    return jsonify(danh_muc)
```

### 5. Ví dụ thực tế

#### Scenario: 3 người dùng cùng sử dụng hệ thống

```
┌──────────────────────────────────────────────────────────┐
│ User: Minh Anh (id=1)                                    │
├──────────────────────────────────────────────────────────┤
│ Email: minhanh@gmail.com                                 │
│ Số dư: 10,000,000 VNĐ                                    │
│ Danh mục:                                                │
│   - Ăn uống (giới hạn: 5tr)                             │
│   - Giải trí (giới hạn: 2tr)                            │
│ Giao dịch:                                               │
│   - 15/01: Chi 500k - Ăn uống                           │
│   - 16/01: Thu 15tr - Lương                             │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ User: Văn Bình (id=2)                                    │
├──────────────────────────────────────────────────────────┤
│ Email: vanbinhh@gmail.com                                │
│ Số dư: 5,000,000 VNĐ                                     │
│ Danh mục:                                                │
│   - Xăng xe (giới hạn: 3tr)                             │
│   - Học phí (giới hạn: 10tr)                            │
│ Giao dịch:                                               │
│   - 15/01: Chi 2tr - Học phí                            │
│   - 17/01: Thu 8tr - Thưởng                             │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ User: Thu Hà (id=3)                                      │
├──────────────────────────────────────────────────────────┤
│ Email: thuha@gmail.com                                   │
│ Số dư: 20,000,000 VNĐ                                    │
│ Danh mục:                                                │
│   - Mua sắm (giới hạn: 8tr)                             │
│   - Du lịch (giới hạn: 15tr)                            │
│ Giao dịch:                                               │
│   - 14/01: Chi 5tr - Mua sắm                            │
│   - 18/01: Chi 10tr - Du lịch                           │
└──────────────────────────────────────────────────────────┘
```

### 6. Queries phân tách dữ liệu

#### 6.1. Lấy giao dịch của user hiện tại
```sql
SELECT gd.*, dm.ten_danh_muc
FROM giao_dich gd
JOIN danh_muc dm ON gd.danh_muc_id = dm.id
WHERE dm.nguoi_dung_id = ?  -- ID user đăng nhập
ORDER BY gd.ngay DESC;
```

#### 6.2. Thống kê chi tiêu của user
```sql
SELECT 
    dm.ten_danh_muc,
    SUM(gd.so_tien) as tong
FROM giao_dich gd
JOIN danh_muc dm ON gd.danh_muc_id = dm.id
WHERE dm.nguoi_dung_id = ?  -- Chỉ user này
    AND dm.loai_danh_muc = 'Chi tiêu'
GROUP BY dm.id;
```

#### 6.3. Kiểm tra vượt giới hạn
```sql
SELECT 
    dm.ten_danh_muc,
    dm.gioi_han,
    SUM(gd.so_tien) as da_chi
FROM giao_dich gd
JOIN danh_muc dm ON gd.danh_muc_id = dm.id
WHERE dm.nguoi_dung_id = ?  -- Riêng user này
GROUP BY dm.id
HAVING SUM(gd.so_tien) > dm.gioi_han;
```

### 7. Bảo mật dữ liệu

#### 7.1. Không thể xem dữ liệu người khác
```python
# User A (id=1) cố truy cập danh mục của User B (id=2)
@app.route('/api/danh-muc/<int:id>')
@token_required
def get_category(current_user, id):
    category = DanhMuc.query.get(id)
    
    # Kiểm tra quyền sở hữu
    if category.nguoi_dung_id != current_user.id:
        return jsonify({'error': 'Không có quyền'}), 403
    
    return jsonify(category)
```

#### 7.2. Cascade Delete an toàn
```sql
-- Khi xóa User A
DELETE FROM nguoi_dung WHERE id = 1;

-- Tự động xóa:
-- ✓ Tất cả danh mục của User A
-- ✓ Tất cả giao dịch của User A
-- ✓ Tất cả tích lũy của User A
-- ✓ Tất cả vay nợ của User A

-- KHÔNG ảnh hưởng:
-- ✗ Dữ liệu của User B, C, D...
```

### 8. Vai trò Admin

```sql
-- Admin (vai_tro_id = 1) có thể:
SELECT * FROM nguoi_dung;  -- Xem tất cả users
UPDATE nguoi_dung SET trang_thai = 'Bị khóa' WHERE id = ?;  -- Khóa user
DELETE FROM nguoi_dung WHERE id = ?;  -- Xóa user

-- User thường (vai_tro_id = 2) chỉ có thể:
-- - Xem/sửa dữ liệu của chính mình
-- - Không thể truy cập dữ liệu người khác
```

### 9. Kiểm tra thực tế

#### Test 1: Đăng ký nhiều user
```bash
# User 1
POST /api/auth/register
{
  "ho_ten": "Nguyễn Văn A",
  "email": "a@gmail.com",
  "mat_khau": "123456"
}

# User 2
POST /api/auth/register
{
  "ho_ten": "Trần Thị B",
  "email": "b@gmail.com",
  "mat_khau": "123456"
}
```

#### Test 2: Mỗi user tạo danh mục riêng
```bash
# User A đăng nhập → token_A
POST /api/danh-muc
Headers: { Authorization: Bearer token_A }
{ "ten_danh_muc": "Ăn uống" }

# User B đăng nhập → token_B
POST /api/danh-muc
Headers: { Authorization: Bearer token_B }
{ "ten_danh_muc": "Học phí" }
```

#### Test 3: Kiểm tra phân tách
```bash
# User A lấy danh mục
GET /api/danh-muc
Headers: { Authorization: Bearer token_A }
→ Chỉ thấy: ["Ăn uống"]

# User B lấy danh mục
GET /api/danh-muc
Headers: { Authorization: Bearer token_B }
→ Chỉ thấy: ["Học phí"]
```

### 10. Kết luận

✅ **Hệ thống hỗ trợ đầy đủ multi-user:**
- Mỗi user có tài khoản riêng (email unique)
- Dữ liệu hoàn toàn phân tách (nguoi_dung_id)
- Bảo mật bằng JWT token
- Không thể xem/sửa dữ liệu người khác
- Admin quản lý tất cả users
- Cascade delete an toàn

✅ **Có thể mở rộng:**
- Thêm 100, 1000, 10000 users
- Mỗi user độc lập hoàn toàn
- Performance tốt nhờ indexes
