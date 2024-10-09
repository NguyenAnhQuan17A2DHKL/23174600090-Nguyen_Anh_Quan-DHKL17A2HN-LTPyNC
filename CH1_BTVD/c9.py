import math

class Da_giac: #Lớp cơ sở cho các đa giác, có phương thức tính chu vi
    def __init__(self, cac_canh):
        self.cac_canh = cac_canh

    def chu_vi(self):
        return sum(self.cac_canh)

class Hinh_binh_hanh(Da_giac): #Lớp kế thừa từ Da_giac và thêm phương thức tính diện tích
    def __init__(self, day, canh, chieu_cao):
        super().__init__([day, canh, day, canh])
        self.day = day
        self.canh = canh
        self.chieu_cao = chieu_cao

    def area(self):
        return self.day * self.chieu_cao

class Hinh_chu_nhat(Hinh_binh_hanh): #Lớp kế thừa từ Hinh_binh_hanh và điều chỉnh phương thức tính diện tích cho hình chữ nhật
    def __init__(self, chieu_rong, chieu_cao):
        super().__init__(chieu_rong, chieu_rong, chieu_cao)
        self.chieu_rong = chieu_rong
        self.chieu_cao = chieu_cao

    def area(self):
        return self.chieu_rong * self.chieu_cao

class Hinh_vuong(Hinh_chu_nhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def area(self):
        return self.canh ** 2

#Nhập số liệu để sử dụng các lớp trên và in ra kết quả:
da_giac = Da_giac([3, 4, 5])
print(f"Chu vi đa giác: {da_giac.chu_vi()}")

hinh_binh_hanh = Hinh_binh_hanh(5, 3, 4)
print(f"Chu vi hình bình hành: {hinh_binh_hanh.chu_vi()}")
print(f"Diện tích hình bình hành: {hinh_binh_hanh.area()}")

hinh_chu_nhat = Hinh_chu_nhat(6, 8)
print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.chu_vi()}")
print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.area()}")

hinh_vuong = Hinh_vuong(6)
print(f"Chu vi hình vuông: {hinh_vuong.chu_vi()}")
print(f"Diện tích hình vuông: {hinh_vuong.area()}")