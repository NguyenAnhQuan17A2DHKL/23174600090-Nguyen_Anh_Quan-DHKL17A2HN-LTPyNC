import sqlite3

#Kết nối với CSDL product.db:
conn = sqlite3.connect("product.db")
cursor = conn.cursor()

#Tạo bảng product:
cursor.execute("""
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
""")
conn.commit()

#Các chức năng:
def display_products():
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        print(product)

def add_product(id, name, price, amount):
    cursor.execute("INSERT INTO product (Id, Name, Price, Amount) VALUES (?, ?, ?, ?)", (id, name, price, amount))
    conn.commit()

def search_product(name):
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    for result in results:
        print(result)

def update_product(id, price, amount):
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (price, amount, id))
    conn.commit()

def delete_product(id):
    cursor.execute("DELETE FROM product WHERE Id = ?", (id,))
    conn.commit()

#Ví dụ sử dụng:
add_product(1, "Laptop", 1500.0, 10)
add_product(2, "Phone", 800.0, 20)
display_products()
search_product("Laptop")
update_product(1, 1400.0, 15)
delete_product(2)
display_products()

conn.close()