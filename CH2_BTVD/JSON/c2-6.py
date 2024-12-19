import json

#JSON string:
json_string = '{"Tên": "Nguyễn Anh Quân", "Tuổi": 19, "is_student": false}'

#Chuyển đổi JSON string thành đối tượng Python:
python_obj = json.loads(json_string)

#In đối tượng Python:
print(python_obj)
print(f"Tên: {python_obj['Tên']}")
print(f"Tuổi: {python_obj['Tuổi']}")
print(f"Là sinh viên: {python_obj['is_student']}")