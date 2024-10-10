import xml.etree.ElementTree as ET

#Tạo root element:
cty = ET.Element("Công ty")

#Tạo các sub-elements:
giamdoc = ET.SubElement(cty, "Giám đốc")
giamdoc.text = "Nguyễn Anh Quân"

diachi = ET.SubElement(cty, "Địa chỉ")
diachi.text = "218 Lĩnh Nam, Quận Hoàng Mai, Hà Nội"

sodienthoai = ET.SubElement(cty, "Số điện thoại")
sodienthoai.text = "0936233908"

masothue = ET.SubElement(cty, "Mã số thuế")
masothue.text = "23174600090"

#Tạo tree và ghi vào file:
tree = ET.ElementTree(cty)
tree.write("Thongtincongty.xml", encoding="utf-8", xml_declaration=True)

#In ra nội dung XML:
ET.dump(cty)