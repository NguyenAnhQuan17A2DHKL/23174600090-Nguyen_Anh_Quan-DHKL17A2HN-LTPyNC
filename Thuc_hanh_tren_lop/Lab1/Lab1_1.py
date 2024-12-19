import xml.etree.ElementTree as ET 

class XMLReader: 
    def __init__(self, file_path): #Phương thức khởi tạo của lớp
        self.file_path = file_path #Tham số được lưu trữ
        self.data = None #Lưu trữ dữ liệu XML đã được phân tích

    def read_xml(self): #Lớp đọc dữ liệu từ file XML
        tree = ET.parse(self.file_path) #Phân tích cú pháp file XML tại đường dẫn self.file_path 
        self.data = tree.getroot() #Lấy phần tử gốc của cây XML và lưu trữ vào thuộc tính self.data

    def display_data(self):
        if self.data: #Kiểm tra xem dữ liệu XML đã được đọc thành công chưa
            for product in self.data.findall('product'): 
                name = product.find('name').text 
                price = product.find('price').text 
                quantity = product.find('quantity').text 
                print(f"Product: {name}, Price: {price}, Quantity: {quantity}") 
                
#Sử dụng lớp XMLReader:
path='C:/Users/SURFACE/Desktop/Uneti/Ki 3/LTPY/Thuc_hanh/DATA//products.xml' 
reader = XMLReader(path) 
reader.read_xml() 
reader.display_data() 