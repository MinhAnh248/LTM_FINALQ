import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app import app, db, NguoiDung, VaiTro
import bcrypt

with app.app_context():
    # Kiểm tra vai trò admin
    admin_role = VaiTro.query.filter_by(loai_vai_tro='admin').first()
    if not admin_role:
        admin_role = VaiTro(id=1, loai_vai_tro='admin', mo_ta='Quản trị viên')
        db.session.add(admin_role)
        db.session.commit()
        print("✓ Đã tạo vai trò admin")
    
    # Kiểm tra tài khoản admin
    admin = NguoiDung.query.filter_by(email='admin@admin.com').first()
    
    if admin:
        # Cập nhật mật khẩu
        hashed = bcrypt.hashpw('123456'.encode('utf-8'), bcrypt.gensalt())
        admin.mat_khau = hashed.decode('utf-8')
        admin.vai_tro_id = 1
        admin.trang_thai = 'Hoạt động'
        db.session.commit()
        print(f"✓ Đã cập nhật tài khoản admin")
        print(f"  Email: admin@admin.com")
        print(f"  Password: 123456")
        print(f"  Vai trò ID: {admin.vai_tro_id}")
    else:
        # Tạo mới
        hashed = bcrypt.hashpw('123456'.encode('utf-8'), bcrypt.gensalt())
        admin = NguoiDung(
            vai_tro_id=1,
            ho_ten='Administrator',
            email='admin@admin.com',
            mat_khau=hashed.decode('utf-8'),
            so_du=0,
            trang_thai='Hoạt động'
        )
        db.session.add(admin)
        db.session.commit()
        print("✓ Đã tạo tài khoản admin mới")
        print(f"  Email: admin@admin.com")
        print(f"  Password: 123456")
    
    # Kiểm tra lại
    admin = NguoiDung.query.filter_by(email='admin@admin.com').first()
    print(f"\n📋 Thông tin admin:")
    print(f"  ID: {admin.id}")
    print(f"  Họ tên: {admin.ho_ten}")
    print(f"  Email: {admin.email}")
    print(f"  Vai trò ID: {admin.vai_tro_id}")
    print(f"  Trạng thái: {admin.trang_thai}")
    
    # Test password
    if bcrypt.checkpw('123456'.encode('utf-8'), admin.mat_khau.encode('utf-8')):
        print(f"  ✓ Mật khẩu đúng")
    else:
        print(f"  ✗ Mật khẩu sai")
