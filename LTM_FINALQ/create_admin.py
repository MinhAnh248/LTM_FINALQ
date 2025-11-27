from app import app, db, NguoiDung, VaiTro
import bcrypt

with app.app_context():
    # Tạo vai trò nếu chưa có
    if not VaiTro.query.first():
        admin_role = VaiTro(loai_vai_tro='admin', mo_ta='Quản trị viên')
        user_role = VaiTro(loai_vai_tro='user', mo_ta='Người dùng')
        db.session.add(admin_role)
        db.session.add(user_role)
        db.session.commit()
    
    # Tạo tài khoản admin
    admin = NguoiDung.query.filter_by(email='admin@admin.com').first()
    if not admin:
        hashed = bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt())
        admin = NguoiDung(
            vai_tro_id=1,
            ho_ten='Administrator',
            email='admin@admin.com',
            mat_khau=hashed.decode('utf-8'),
            so_du=0
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin created!')
        print('Email: admin@admin.com')
        print('Password: admin123')
    else:
        print('Admin exists!')
