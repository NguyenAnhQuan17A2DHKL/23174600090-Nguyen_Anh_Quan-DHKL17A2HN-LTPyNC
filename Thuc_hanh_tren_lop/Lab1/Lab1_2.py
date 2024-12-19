import json

class JSONReader: #Lớp đọc và xử lý dữ liệu từ một file JSON
    def __init__(self, file_path): 
        self.file_path = file_path 
        self.data = None 

    def read_json(self): #Lớp đọc dữ liệu từ file JSON
        with open(self.file_path, 'r') as file: #Sử dụng khối lệnh with để mở file JSON với chế độ đọc ('r')
            self.data = json.load(file) #Sử dụng hàm load của thư viện json để đọc nội dung của file và chuyển đổi nó thành một cấu trúc dữ liệu Python

    def display_data(self): 
        if self.data: #Kiểm tra xem dữ liệu JSON đã được đọc thành công chưa
            for user in self.data: #Lặp qua từng đối tượng người dùng trong dữ liệu JSON đã được đọc
                print(f"Name: {user['name']}, Age: {user['age']}, \ Address:{user['address']}") 

#Sử dụng lớp JSONReader:
path = 'C:/Users/SURFACE/Desktop/Uneti/Ki 3/LTPY/Thuc_hanh/DATA//users.json' 
reader = JSONReader(path) 
reader.read_json() 
reader.display_data()