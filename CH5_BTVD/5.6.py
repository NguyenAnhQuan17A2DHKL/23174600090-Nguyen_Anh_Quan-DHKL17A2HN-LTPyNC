import sqlite3

#Kết nối tới cơ sở dữ liệu:
conn = sqlite3.connect('example.db')

#Đếm số bản ghi:
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]

print(f"Số lượng bản ghi trong bảng 'products': {count}")

#Đóng kết nối:
conn.close()