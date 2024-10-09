class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa): #Hàm lưu trữ các thông tin của TS
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self): #Hàm nhập thông tin
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def in_thong_tin(self): #Hàm in ra thông tin
        print(f"Họ tên: {self.ho_ten}, Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hóa: {self.diem_hoa}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

#Chương trình chính:
danh_sach_thi_sinh = []

#Nhập thông tin thí sinh:
so_luong_thi_sinh = int(input("Nhập số lượng thí sinh: "))
for _ in range(so_luong_thi_sinh):
    thi_sinh = TS("", 0, 0, 0)
    thi_sinh.nhap_thong_tin()
    danh_sach_thi_sinh.append(thi_sinh)

#Sắp xếp danh sách thí sinh theo tổng điểm từ cao xuống thấp:
danh_sach_thi_sinh.sort(key = lambda ts: ts.tinh_tong_diem(), reverse = True)

#In danh sách thí sinh trúng tuyển:
print("Danh sách thí sinh trúng tuyển: ")
for thi_sinh in danh_sach_thi_sinh:
    if thi_sinh.tinh_tong_diem() >= 20:
        thi_sinh.in_thong_tin()