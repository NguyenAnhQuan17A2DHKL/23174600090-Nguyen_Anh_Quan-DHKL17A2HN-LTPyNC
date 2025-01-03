import sqlite3

#Kết nối tới cơ sở dữ liệu:
conn = sqlite3.connect('example.db')

#Cập nhật giá trị của một cột:
cursor = conn.cursor()
cursor.execute("UPDATE products SET price = price + 0.1")
conn.commit()

print("Tất cả giá trị của cột 'price' đã được cập nhật.")

#Kiểm tra kết quả:
cursor.execute("SELECT * FROM products")
records = cursor.fetchall()
print("Dữ liệu sau khi cập nhật:")
for record in records:
    print(record)

#Đóng kết nối:
conn.close()