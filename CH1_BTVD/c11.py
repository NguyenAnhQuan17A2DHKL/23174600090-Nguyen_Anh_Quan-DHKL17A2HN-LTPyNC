import math

class Tam_giac: #Lớp cơ sở với các thuộc tính a, b, c để lưu trữ độ dài các cạnh của tam giác
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def chu_vi(self): #Hàm tính chu vi
        return self.a + self.b + self.c

    def dien_tich(self): #Hàm tính diện tích
        s = self.chu_vi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Tam_giac_vuong(Tam_giac): #Lớp kế thừa từ Tam_giac và thêm phương thức tính diện tích cho tam giác vuông
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

    def dien_tich(self):
        return 0.5 * self.a * self.b

class Tam_giac_can(Tam_giac): #Lớp kế thừa từ Tam_giac và sử dụng hai cạnh bằng nhau
    def __init__(self, a, b):
        super().__init__(a, a, b)

class Tam_giac_deu(Tam_giac_can): #Lớp kế thừa từ Tam_giac_can và sử dụng ba cạnh bằng nhau
    def __init__(self, a):
        super().__init__(a, a)

    def dien_tich(self):
        return (math.sqrt(3) / 4) * self.a**2

#Nhập số liệu để sử dụng các lớp trên và in ra kết quả:
tam_giac = Tam_giac(3, 4, 5)
print(f"Chu vi tam giác: {tam_giac.chu_vi()}")
print(f"Diện tích tam giác: {tam_giac.dien_tich()}")

tam_giac_vuong = Tam_giac_vuong(3, 4)
print(f"Chu vi tam giác vuông: {tam_giac_vuong.chu_vi()}")
print(f"Diện tích tam giác vuông: {tam_giac_vuong.dien_tich()}")

tam_giac_can = Tam_giac_can(5, 8)
print(f"Chu vi tam giác cân: {tam_giac_can.chu_vi()}")
print(f"Diện tích tam giác cân: {tam_giac_can.dien_tich()}")

tam_giac_deu = Tam_giac_deu(6)
print(f"Chu vi tam giác đều: {tam_giac_deu.chu_vi()}")
print(f"Diện tích tam giác đều: {tam_giac_deu.dien_tich()}")