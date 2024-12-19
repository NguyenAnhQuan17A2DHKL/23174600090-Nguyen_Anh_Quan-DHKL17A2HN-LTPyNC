from xml.dom import minidom

#Tải và phân tích tệp XML:
doc = minidom.parse("sample.xml")

#Lấy danh sách các phần tử 'staff':
staff_list = doc.getElementsByTagName("staff")

#In ra tên của mỗi phần tử:
for staff in staff_list:
    name = staff.getElementsByTagName("name")[0].firstChild.data
    print(name)