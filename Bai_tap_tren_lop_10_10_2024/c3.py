from xml.dom import minidom

#Tải và phân tích file XML:
doc = minidom.parse("sample.xml")

#Lấy root element:
company = doc.documentElement

#Lấy tên công ty:
company_name = company.getElementsByTagName("name")[0].firstChild.data
print("Company Name:", company_name)

#Lấy danh sách nhân viên:
staffs = company.getElementsByTagName("staff")

for staff in staffs:
    staff_id = staff.getAttribute("id")
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {staff_id}, Name: {name}, Salary: {salary}")