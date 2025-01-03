import sqlite3

#Kết nối tới cơ sở dữ liệu:
conn = sqlite3.connect('example.db')

#Xóa một hàng cụ thể:
cursor = conn.cursor()
cursor.execute("DELETE FROM products WHERE name = 'Banana'")
conn.commit()

print("Hàng với tên 'Banana' đã được xóa.")

#Kiểm tra kết quả:
cursor.execute("SELECT * FROM products")
records = cursor.fetchall()
print("Dữ liệu sau khi xóa:")
for record in records:
    print(record)

#Đóng kết nối:
conn.close()