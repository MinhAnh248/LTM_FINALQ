# Hướng dẫn Deploy lên Render

## 1. Chuẩn bị

- Tạo tài khoản GitHub (nếu chưa có)
- Tạo tài khoản Render tại https://render.com

## 2. Push code lên GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/expense-tracker.git
git push -u origin main
```

## 3. Deploy Backend lên Render

1. Đăng nhập vào https://render.com
2. Click "New +" → "Web Service"
3. Connect GitHub repository của bạn
4. Cấu hình:
   - **Name**: expense-tracker-backend
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free
5. Click "Create Web Service"
6. Đợi deploy xong, copy URL (ví dụ: https://expense-tracker-backend.onrender.com)

## 4. Deploy Frontend lên Render (Static Site)

1. Click "New +" → "Static Site"
2. Connect cùng GitHub repository
3. Cấu hình:
   - **Name**: expense-tracker-frontend
   - **Build Command**: (để trống)
   - **Publish Directory**: `.`
4. Click "Create Static Site"
5. Copy URL frontend (ví dụ: https://expense-tracker-frontend.onrender.com)

## 5. Cập nhật API URL trong Frontend

Thay tất cả `http://localhost:5000` trong các file HTML thành URL backend từ Render:

- `index.html`
- `admin.html`
- `ocr_hoadon.html`

Ví dụ:
```javascript
// Thay đổi từ:
const API_URL = 'http://localhost:5000/api';

// Thành:
const API_URL = 'https://expense-tracker-backend.onrender.com/api';
```

## 6. Commit và Push lại

```bash
git add .
git commit -m "Update API URL for production"
git push
```

Render sẽ tự động deploy lại!

## 7. Truy cập ứng dụng

- Frontend: https://expense-tracker-frontend.onrender.com
- Backend API: https://expense-tracker-backend.onrender.com/api

## Lưu ý

- Free tier của Render sẽ sleep sau 15 phút không hoạt động
- Lần đầu truy cập sau khi sleep sẽ mất ~30 giây để wake up
- Database SQLite sẽ bị reset mỗi khi deploy lại (nên dùng PostgreSQL cho production)
