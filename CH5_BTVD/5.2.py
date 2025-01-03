import sqlite3

#Tạo kết nối đến cơ sở dữ liệu trong bộ nhớ:
conn = sqlite3.connect(':memory:')
print("Kết nối tới cơ sở dữ liệu SQLite trong bộ nhớ thành công.")

#Đóng kết nối:
conn.close()