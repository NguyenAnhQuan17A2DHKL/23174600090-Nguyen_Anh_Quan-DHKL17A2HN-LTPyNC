import tkinter as tk
from tkinter import messagebox
import sqlite3

#Kết nối với cơ sở dữ liệu SQLite:
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

#Tạo bảng sản phẩm:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
''')
conn.commit()

#Hàm thêm sản phẩm vào cơ sở dữ liệu:
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    if name and price:
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, float(price)))
        conn.commit()
        update_product_list()
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

#Hàm tìm kiếm sản phẩm:
def search_product():
    name = entry_search.get()
    if name:
        cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        display_products(rows)
    else:
        update_product_list()

#Hàm cập nhật danh sách sản phẩm:
def update_product_list():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    display_products(rows)

#Hàm hiển thị danh sách sản phẩm:
def display_products(rows):
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")

#Hàm xóa sản phẩm:
def delete_product():
    try:
        selected_item = listbox.get(listbox.curselection())
        product_id = int(selected_item.split(",")[0].split(":")[1].strip())
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        update_product_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a product to delete")

#Tạo cửa sổ chính:
root = tk.Tk()
root.title("Product Management")

#Tạo các widget:
label_name = tk.Label(root, text="Product Name:")
label_name.grid(row=0, column=0)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_price = tk.Label(root, text="Product Price:")
label_price.grid(row=1, column=0)

entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

button_add = tk.Button(root, text="Add Product", command=add_product)
button_add.grid(row=2, column=0, columnspan=2)

label_search = tk.Label(root, text="Search Product:")
label_search.grid(row=3, column=0)

entry_search = tk.Entry(root)
entry_search.grid(row=3, column=1)

button_search = tk.Button(root, text="Search", command=search_product)
button_search.grid(row=4, column=0, columnspan=2)

button_delete = tk.Button(root, text="Delete Product", command=delete_product)
button_delete.grid(row=5, column=0, columnspan=2)

#Tạo Listbox để hiển thị sản phẩm:
listbox = tk.Listbox(root, width=50, height=10)
listbox.grid(row=6, column=0, columnspan=2)

#Cập nhật danh sách sản phẩm ban đầu:
update_product_list()

#Chạy ứng dụng:
root.mainloop()

#Đóng kết nối khi thoát:
conn.close()