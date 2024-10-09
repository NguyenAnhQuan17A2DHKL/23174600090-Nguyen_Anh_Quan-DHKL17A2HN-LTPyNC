class PS:
    def __init__(self, tu = 0, mau = 1): 
        self.tu = tu
        self.mau = mau

    def hop_le(self):
        return self.mau != 0

    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        while True:
            self.mau = int(input("Nhập mẫu số (Khác 0): "))
            if self.mau != 0:
                break
            print("Mẫu số phải khác 0. Yêu cầu nhập lại")

    def in_ra(self):
        if self.mau == 1:
            print(self.tu)
        else:
            print(f"{self.tu}/{self.mau}")

#Sử dụng lớp PS:
ps = PS()
ps.nhap()
if ps.hop_le():
    print("Phân số vừa nhập là: ", end="")
    ps.in_ra()
else:
    print("Phân số không hợp lệ")