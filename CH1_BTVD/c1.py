class HCN:
    def __init__(self, chieu_dai = 0, chieu_rong = 0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def nhap_data(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def in_thong_tin(self):
        print(f"Chiều dài: {self.chieu_dai}")
        print(f"Chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

#Chương trình chính:
hinh_chu_nhat = HCN()
hinh_chu_nhat.nhap_data()
hinh_chu_nhat.in_thong_tin()