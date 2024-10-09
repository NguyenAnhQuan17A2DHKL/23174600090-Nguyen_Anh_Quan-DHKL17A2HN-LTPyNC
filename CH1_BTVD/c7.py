class Date:
    def __init__(self, ngay = 1, thang = 1, nam = 2000): #Hàm khởi tạo đối tượng Date với các giá trị mặc định cho ngày, tháng và năm
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self): #Hàm in ra ngày tháng năm theo định dạng dd-mm-yyyy
        print(f"{self.ngay:02d}-{self.thang:02d}-{self.nam}")

    def next(self): #Hàm tính toán ngày tiếp theo và xử lý năm nhuận
        #Số ngày trong mỗi tháng:
        ngay_trong_moi_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #Kiểm tra năm nhuận:
        if (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0):
            ngay_trong_moi_thang[1] = 29

        self.ngay += 1

        if self.ngay > ngay_trong_moi_thang[self.thang - 1]:
            self.ngay = 1
            self.thang += 1

            if self.thang > 12:
                self.thang = 1
                self.nam += 1

#Nhập giá trị bất kì để sử dụng lớp Date và in ra kết quả:
date = Date(28, 1, 2005)
date.display()  # In ra: 31-12-2023
date.next()
date.display()  # In ra: 01-01-2024