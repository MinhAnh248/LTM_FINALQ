import sys
import io
sys.path.insert(0, 'd:\\LTM_FINALQ')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app import app, db, NguoiDung, DanhMuc

with app.app_context():
    # Lấy tất cả user chưa có danh mục
    users = NguoiDung.query.all()
    
    default_categories = [
        {'loai': 'Chi tiêu', 'ten': 'Ăn uống', 'icon': '🍔'},
        {'loai': 'Chi tiêu', 'ten': 'Giải trí', 'icon': '🎮'},
        {'loai': 'Chi tiêu', 'ten': 'Mua sắm', 'icon': '🛒'},
        {'loai': 'Chi tiêu', 'ten': 'Di chuyển', 'icon': '🚗'},
        {'loai': 'Thu nhập', 'ten': 'Lương', 'icon': '💰'},
        {'loai': 'Thu nhập', 'ten': 'Thưởng', 'icon': '🎁'},
    ]
    
    for user in users:
        # Kiểm tra user đã có danh mục chưa
        existing = DanhMuc.query.filter_by(nguoi_dung_id=user.id).count()
        
        if existing == 0:
            print(f"Thêm danh mục cho user: {user.email}")
            for cat in default_categories:
                danh_muc = DanhMuc(
                    nguoi_dung_id=user.id,
                    loai_danh_muc=cat['loai'],
                    ten_danh_muc=cat['ten'],
                    icon=cat['icon']
                )
                db.session.add(danh_muc)
            db.session.commit()
            print(f"✓ Đã thêm {len(default_categories)} danh mục")
        else:
            print(f"User {user.email} đã có {existing} danh mục")
    
    print("\n✓ Hoàn tất!")
