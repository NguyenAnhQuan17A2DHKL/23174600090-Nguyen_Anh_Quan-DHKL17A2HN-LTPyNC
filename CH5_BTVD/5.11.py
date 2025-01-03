import sqlite3

conn = sqlite3.connect("qly_nhan_vien.db")
cursor = conn.cursor()

#Tạo bảng PHONG:
cursor.execute("""
CREATE TABLE IF NOT EXISTS PHONG (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
""")

#Tạo bảng NHAN_VIEN:
cursor.execute("""
CREATE TABLE IF NOT EXISTS NHAN_VIEN (
    id INTEGER PRIMARY KEY,
    ho_ten TEXT NOT NULL,
    tuoi INTEGER NOT NULL,
    dia_chi TEXT NOT NULL,
    luong REAL NOT NULL,
    Id_phong INTEGER,
    FOREIGN KEY (Id_phong) REFERENCES PHONG (Id)
)
""")
conn.commit()

#Các chức năng:
def add_phong(id, name):
    cursor.execute("INSERT INTO PHONG (Id, Name) VALUES (?, ?)", (id, name))
    conn.commit()

def add_nhan_vien(id, ho_ten, tuoi, dia_chi, luong, id_phong):
    cursor.execute("INSERT INTO NHAN_VIEN (id, ho_ten, tuoi, dia_chi, luong, Id_phong) VALUES (?, ?, ?, ?, ?, ?)", 
                   (id, ho_ten, tuoi, dia_chi, luong, id_phong))
    conn.commit()

def display_phong():
    cursor.execute("SELECT * FROM PHONG")
    for phong in cursor.fetchall():
        print(phong)

def display_nhan_vien():
    cursor.execute("SELECT * FROM NHAN_VIEN")
    for nhan_vien in cursor.fetchall():
        print(nhan_vien)



conn.close()