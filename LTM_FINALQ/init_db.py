from app_complete import app, db
from models import VaiTro

with app.app_context():
    db.create_all()
    
    if not VaiTro.query.first():
        admin = VaiTro(loai_vai_tro='admin', mo_ta='Quản trị viên')
        user = VaiTro(loai_vai_tro='user', mo_ta='Người dùng')
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()
        print('Khoi tao database thanh cong!')
    else:
        print('Database da ton tai!')
