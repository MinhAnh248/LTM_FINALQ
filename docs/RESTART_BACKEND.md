# HƯỚNG DẪN KHỞI ĐỘNG LẠI BACKEND

## ✅ Đã sửa xong các lỗi:

1. **JWT identity** - Đã chuyển sang string
2. **Tự động tạo danh mục** - User mới sẽ có 6 danh mục mặc định
3. **User cũ** - Đã thêm danh mục cho tất cả user hiện tại

## 🔄 Khởi động lại backend:

### Cách 1: Dùng script
```bash
# Dừng backend hiện tại (Ctrl+C)
# Chạy lại
python app.py
```

### Cách 2: Dùng file bat
```bash
run.bat
```

## 🧪 Test sau khi khởi động:

1. **Mở trình duyệt** → http://localhost:5000 (hoặc mở index.html)
2. **Đăng nhập** với tài khoản: minhanh@gmail.com / 123456
3. **Vào tab "Giao Dịch"**
4. **Click dropdown "Danh Mục"** → Sẽ thấy:
   ```
   📸 Chi Tiêu
     🍔 Ăn uống
     🎮 Giải trí
     🛒 Mua sắm
     🚗 Di chuyển
   
   💰 Thu Nhập
     💰 Lương
     🎁 Thưởng
   ```

5. **Chọn danh mục** → Nhập số tiền → Nhập mô tả → **Thêm Giao Dịch**

## ✅ Kết quả mong đợi:

- Dropdown có danh mục để chọn ✓
- Có thể thêm giao dịch thành công ✓
- Số dư tự động cập nhật ✓
