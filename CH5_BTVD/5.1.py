import sqlite3

#Tạo hoặc kết nối với cơ sở dữ liệu SQLite:
conn = sqlite3.connect('example.db')

#Lấy thông tin version SQLite:
cursor = conn.cursor()
cursor.execute('SELECT SQLITE_VERSION()')
version = cursor.fetchone()[0]

print(f"Version của SQLite: {version}")

#Đóng kết nối:
conn.close()