import xml.etree.ElementTree as ET

#Tạo root element:
Thong_tin_sinh_vien = ET.Element("Thong_tin_sinh_vien")

#Thêm thông tin sinh viên:
def them_sinh_vien(ma_sv, ten, ngay_sinh, lop, gioi_tinh):
    student = ET.SubElement(Thong_tin_sinh_vien, "Student")
    
    ma_sv_elem = ET.SubElement(student, "Mã sinh viên")
    ma_sv_elem.text = ma_sv
    
    ten_elem = ET.SubElement(student, "Tên")
    ten_elem.text = ten
    
    ngay_sinh_elem = ET.SubElement(student, "Ngày sinh")
    ngay_sinh_elem.text = ngay_sinh
    
    class_elem = ET.SubElement(student, "Lớp")
    class_elem.text = lop
    
    gioi_tinh_elem = ET.SubElement(student, "Giới tính")
    gioi_tinh_elem.text = gioi_tinh

#Thêm một số sinh viên vào danh sách:
them_sinh_vien("23174600090", "Nguyễn Anh Quân", "2005", "DHKL17A2HN", "Nam")
them_sinh_vien("SV2", "Nguyễn Văn A", "2005", "DHKL17A3HN", "Nam")
them_sinh_vien("SV3", "Phạm Thị B", "2005", "DHKL17A1HN", "Nữ")

#Tạo tree và ghi vào file:
tree = ET.ElementTree(Thong_tin_sinh_vien)
tree.write("Thong_tin_sinh_vien.xml", encoding="utf-8", xml_declaration=True)

#In ra nội dung XML:
ET.dump(Thong_tin_sinh_vien)