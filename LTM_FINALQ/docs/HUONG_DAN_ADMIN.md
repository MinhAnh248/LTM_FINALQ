# HƯỚNG DẪN CHẠY HỆ THỐNG ADMIN

## 🎯 Kiến trúc 2 Backend riêng biệt:

```
┌─────────────────────────────────────────────────┐
│  USER BACKEND (Port 5000)                       │
│  - Đăng ký/Đăng nhập user                       │
│  - Quản lý giao dịch                            │
│  - Quản lý danh mục                             │
│  - Thống kê cá nhân                             │
│  File: app.py                                   │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  ADMIN BACKEND (Port 5111)                      │
│  - Đăng nhập admin                              │
│  - Quản lý tất cả user                          │
│  - Khóa/Mở khóa tài khoản                       │
│  - Xóa user                                     │
│  - Thống kê hệ thống                            │
│  File: app_admin.py                             │
└─────────────────────────────────────────────────┘
```

## 🚀 Cách chạy:

### 1. Chạy User Backend (Port 5000)
```bash
# Terminal 1
python app.py
```
Hoặc:
```bash
run.bat
```

### 2. Chạy Admin Backend (Port 5111)
```bash
# Terminal 2 (mở terminal mới)
python app_admin.py
```
Hoặc:
```bash
run_admin.bat
```

## 🌐 Truy cập:

### User Interface
- URL: `http://localhost:5000` hoặc mở `index.html`
- Backend: Port 5000
- Tài khoản: user@gmail.com / 123456

### Admin Interface
- URL: Mở file `admin.html` trong trình duyệt
- Backend: Port 5111
- Tài khoản: admin@admin.com / 123456

## 🔐 Tài khoản Admin mặc định:

```
Email: admin@admin.com
Password: 123456
```

## ✅ Kiểm tra Backend đang chạy:

### User Backend (5000):
```bash
curl http://localhost:5000/api/danh-muc
```

### Admin Backend (5111):
```bash
curl http://localhost:5111/api/admin/users
```

## 📋 API Endpoints Admin:

```
POST   /api/auth/login              - Đăng nhập admin
GET    /api/admin/users             - Lấy danh sách user
PUT    /api/admin/users/:id/lock    - Khóa user
PUT    /api/admin/users/:id/unlock  - Mở khóa user
DELETE /api/admin/users/:id         - Xóa user
GET    /api/admin/stats             - Thống kê hệ thống
```

## 🔧 Troubleshooting:

### Lỗi: Port 5111 đã được sử dụng
```bash
# Windows
netstat -ano | findstr :5111
taskkill /PID <PID> /F
```

### Lỗi: Không kết nối được
- Kiểm tra backend admin đang chạy
- Kiểm tra CORS đã bật
- Xóa token cũ: `localStorage.clear()`

## 🎨 Tính năng Admin:

✅ Xem danh sách tất cả user
✅ Khóa/Mở khóa tài khoản user
✅ Xem số dư của từng user
✅ Thống kê tổng quan hệ thống
✅ Bảo mật: Chỉ admin mới truy cập được

## 📊 Database chung:

Cả 2 backend đều dùng chung 1 database:
```
instance/expense.db
```

Vì vậy dữ liệu đồng bộ giữa user và admin!
