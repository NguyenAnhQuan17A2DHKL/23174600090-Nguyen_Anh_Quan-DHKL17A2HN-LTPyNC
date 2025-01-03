import sqlite3

#Kết nối tới cơ sở dữ liệu:
conn = sqlite3.connect('example.db')

#Tạo bảng:
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')
print("Bảng 'students' đã được tạo.")

#Đóng kết nối:
conn.close()