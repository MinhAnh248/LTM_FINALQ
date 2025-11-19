import sqlite3
import sys
import io

# Fix encoding cho Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Kết nối database
conn = sqlite3.connect('instance/expense.db')
cursor = conn.cursor()

# Lấy danh sách bảng
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("=" * 80)
print("DATABASE SCHEMA - HE THONG QUAN LY CHI TIEU")
print("=" * 80)

for table in tables:
    table_name = table[0]
    print(f"\n--- Bảng: {table_name} ---")
    
    # Lấy schema
    cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    schema = cursor.fetchone()[0]
    print(schema)
    
    # Đếm số dòng
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = cursor.fetchone()[0]
    print(f"\n-- Số dòng dữ liệu: {count}")
    
    # Hiển thị 3 dòng mẫu
    if count > 0:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 3;")
        rows = cursor.fetchall()
        print(f"-- Dữ liệu mẫu:")
        for row in rows:
            print(f"--   {row}")

print("\n" + "=" * 80)
print("INDEXES")
print("=" * 80)
cursor.execute("SELECT sql FROM sqlite_master WHERE type='index' AND sql IS NOT NULL;")
indexes = cursor.fetchall()
for idx in indexes:
    print(idx[0])

conn.close()
print("\n✓ Export hoàn tất!")
