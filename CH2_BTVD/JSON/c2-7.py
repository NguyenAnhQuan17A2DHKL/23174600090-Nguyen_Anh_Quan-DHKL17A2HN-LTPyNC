import json

#Đối tượng Python (từ điển):
python_obj = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"]
}

#Chuyển đổi đối tượng Python sang chuỗi JSON:
json_string = json.dumps(python_obj, indent=4)

#In chuỗi JSON:
print("Chuỗi JSON:")
print(json_string)

#In ra tất cả các giá trị trong đối tượng Python:
print("\nCác giá trị trong đối tượng Python:")
for key, value in python_obj.items():
    print(f"{key}: {value}")
