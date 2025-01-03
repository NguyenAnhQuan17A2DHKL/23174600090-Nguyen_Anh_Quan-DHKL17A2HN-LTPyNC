import sqlite3

#Kết nối tới cơ sở dữ liệu:
conn = sqlite3.connect('example.db')

#Liệt kê các bảng:
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Các bảng trong cơ sở dữ liệu:")
for table in tables:
    print(table[0])

#Đóng kết nối:
conn.close()