# Hệ Thống Quản Lý Chi Tiêu

Ứng dụng web quản lý chi tiêu cá nhân với các tính năng theo dõi giao dịch, quản lý danh mục, thống kê chi tiêu.

## Cài Đặt

### Backend
```bash
pip install -r requirements.txt
python app.py
```

Backend chạy trên `http://localhost:5000`

### Frontend
Mở file `index.html` trong trình duyệt hoặc sử dụng live server.

## Tính Năng

- **Đăng Ký/Đăng Nhập**: Tạo tài khoản và xác thực người dùng
- **Quản Lý Giao Dịch**: Thêm, xem lịch sử chi tiêu và thu nhập
- **Quản Lý Danh Mục**: Tạo danh mục chi tiêu và thu nhập
- **Thống Kê**: Xem báo cáo chi tiêu theo tháng
- **Hồ Sơ Cá Nhân**: Cập nhật thông tin người dùng

## API Endpoints

### Auth
- `POST /api/auth/register` - Đăng ký
- `POST /api/auth/login` - Đăng nhập

### Transactions
- `POST /api/giao-dich` - Thêm giao dịch
- `GET /api/giao-dich` - Lấy danh sách giao dịch

### Categories
- `POST /api/danh-muc` - Tạo danh mục
- `GET /api/danh-muc` - Lấy danh sách danh mục

### User
- `GET /api/user/profile` - Lấy hồ sơ
- `PUT /api/user/profile` - Cập nhật hồ sơ

### Statistics
- `GET /api/thong-ke` - Lấy thống kê

## Cấu Trúc Project

```
├── app.py              # File chính Flask
├── models.py           # Database models
├── routes.py           # API routes
├── config.py           # Cấu hình
├── index.html          # Frontend
├── requirements.txt    # Dependencies
└── .env               # Biến môi trường
```

## Công Nghệ

- **Backend**: Flask, SQLAlchemy, JWT
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
