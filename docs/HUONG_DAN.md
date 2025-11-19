# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG QUẢN LÝ CHI TIÊU

## Khởi động dự án

### Cách 1: Sử dụng file start.bat
```
Nhấp đúp vào file start.bat
```

### Cách 2: Chạy thủ công
```bash
python app.py
```

## Truy cập hệ thống

1. **Backend API**: http://localhost:5000
2. **Frontend Người dùng**: Mở file `index.html` trong trình duyệt
3. **Frontend Admin**: Mở file `admin.html` trong trình duyệt

## Tài khoản mặc định

**Admin:**
- Email: `admin@admin.com`
- Password: `admin123`

## Các chức năng đã triển khai

### 1. Xác thực
- ✅ Đăng ký tài khoản
- ✅ Đăng nhập
- ✅ Quản lý hồ sơ cá nhân

### 2. Quản lý giao dịch
- ✅ Thêm giao dịch thu/chi
- ✅ Xem lịch sử giao dịch
- ✅ Tính toán số dư tự động

### 3. Quản lý danh mục
- ✅ Tạo danh mục chi tiêu/thu nhập
- ✅ Đặt giới hạn chi tiêu cho danh mục
- ✅ Cảnh báo vượt mức

### 4. Thống kê
- ✅ Thống kê theo tháng/năm
- ✅ Báo cáo chi tiết theo danh mục
- ✅ Phân tích xu hướng

### 5. Quản lý vay nợ
- ✅ Thêm khoản vay/nợ
- ✅ Thanh toán từng phần
- ✅ Nhắc nhở đến hạn

### 6. Tiết kiệm
- ✅ Tạo mục tiêu tiết kiệm
- ✅ Theo dõi tiến độ
- ✅ Lịch sử tích lũy

### 7. Quản trị hệ thống (Admin)
- ✅ Xem danh sách người dùng
- ✅ Khóa/Mở khóa tài khoản
- ✅ Thống kê tổng quan hệ thống

## API Endpoints

### Auth
- POST `/api/auth/register` - Đăng ký
- POST `/api/auth/login` - Đăng nhập

### Giao dịch
- GET `/api/giao-dich` - Danh sách giao dịch
- POST `/api/giao-dich` - Thêm giao dịch

### Danh mục
- GET `/api/danh-muc` - Danh sách danh mục
- POST `/api/danh-muc` - Thêm danh mục
- POST `/api/gioi-han-chi-tieu` - Đặt giới hạn

### Vay nợ
- GET `/api/vay-no` - Danh sách vay nợ
- POST `/api/vay-no` - Thêm vay nợ
- POST `/api/thanh-toan` - Thanh toán

### Tiết kiệm
- GET `/api/tich-luy` - Danh sách tiết kiệm
- POST `/api/tich-luy` - Thêm mục tiêu
- GET `/api/lich-su-tich-luy/<id>` - Lịch sử

### Thống kê
- GET `/api/thong-ke` - Thống kê tổng quan
- GET `/api/thong-ke-chi-tiet` - Thống kê chi tiết
- GET `/api/nhac-nho` - Nhắc nhở thanh toán

### Admin
- GET `/api/admin/users` - Danh sách người dùng
- PUT `/api/admin/users/<id>/lock` - Khóa tài khoản
- PUT `/api/admin/users/<id>/unlock` - Mở khóa tài khoản

## Bảo mật & Phân quyền

### Bảo mật dữ liệu
- ✅ Mật khẩu được mã hóa bằng bcrypt
- ✅ Xác thực JWT token
- ✅ CORS được cấu hình chặt chẽ
- ✅ Kiểm tra tài khoản bị khóa tự động

### Phân quyền
- **Admin**: Quản lý tất cả người dùng, khóa/mở khóa tài khoản
- **User**: Chỉ xem và quản lý dữ liệu của mình

### Tính tương thích
- ✅ Responsive design cho mobile/tablet/desktop
- ✅ Hỗ trợ tất cả trình duyệt hiện đại
- ✅ Giao diện thân thiện, dễ sử dụng

## Lưu ý
- Backend chạy trên port 5000
- Database: SQLite (expense.db)
- Token JWT hết hạn sau 30 ngày
- Xem chi tiết bảo mật trong file `BAO_MAT.md`

## Khuyến nghị
1. Thay đổi mật khẩu admin mặc định
2. Sử dụng mật khẩu mạnh (8+ ký tự)
3. Đăng xuất sau khi sử dụng
4. Backup database thường xuyên

## Tài liệu tham khảo
- `BAO_MAT.md` - Chi tiết về bảo mật hệ thống
- `QUY_TRINH_SCRUM.md` - Quy trình Scrum đã áp dụng
- `PHAN_CONG_VAI_TRO.md` - Phân công vai trò chi tiết
- `BACKLOG_ARTIFACTS.md` - Product Backlog, Sprint Backlog, DoD
- `README.md` - Thông tin tổng quan dự án
