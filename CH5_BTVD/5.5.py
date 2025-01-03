import sqlite3

#Kết nối tới cơ sở dữ liệu:
conn = sqlite3.connect('example.db')

#Tạo bảng:
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL
    )
''')
print("Bảng 'products' đã được tạo.")

#Chèn dữ liệu vào bảng:
cursor.execute("INSERT INTO products (name, price) VALUES ('Apple', 0.5)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Banana', 0.3)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Cherry', 1.0)")
conn.commit()
print("Dữ liệu đã được chèn vào bảng.")

#Lấy tất cả các bản ghi:
cursor.execute("SELECT * FROM products")
records = cursor.fetchall()
print("Các bản ghi trong bảng 'products':")
for record in records:
    print(record)

#Đóng kết nối:
conn.close()