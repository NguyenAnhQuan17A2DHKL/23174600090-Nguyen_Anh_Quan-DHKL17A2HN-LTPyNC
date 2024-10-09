import math

class Diem: #Lớp cơ sở với các thuộc tính x và y để lưu trữ tọa độ của điểm
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Diem({self.x}, {self.y})")

class Elip(Diem): #Lớp kế thừa từ lớp Diem và thêm các thuộc tính truc_lon và truc_nho để lưu trữ trục lớn và trục nhỏ của elip
    def __init__(self, x, y, truc_lon, truc_nho):
        super().__init__(x, y)
        self.truc_lon = truc_lon
        self.truc_nho = truc_nho

    def dien_tich(self): #Hàm tính diện tích của Elip
        return math.pi * self.truc_lon * self.truc_nho

    def display(self): #Hàm in ra kết quả của Elip
        super().display()
        print(f"Elip với trục lớn: {self.truc_lon}, trục nhỏ: {self.truc_nho}")
        print(f"Diện tích: {self.dien_tich()}")

class Hinh_tron(Elip): #Hàm kế thừa từ Elip và sử dụng cùng 1 giá trị cho trục lớn và trục nhỏ (Bán kính) để biểu diễn đường tròn
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius)
        self.radius = radius

    def display(self): #Hàm in ra kết quả của Hinh_tron
        super().display()
        print(f"Bán kính hình tròn: {self.radius}")
        print(f"Diện tích: {self.dien_tich()}")

#Nhập giá trị để sử dụng các lớp trên và in ra kết quả:
diem = Diem(1, 2)
diem.display()

elip = Elip(1, 2, 3, 4)
elip.display()

hinh_tron = Hinh_tron(1, 2, 3)
hinh_tron.display()