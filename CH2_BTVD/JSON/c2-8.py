import json

#Đối tượng từ điển Python
python_dict = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"]
}

#Chuyển đổi đối tượng từ điển Python sang chuỗi JSON với các khóa được sắp xếp
json_string = json.dumps(python_dict, indent=4, sort_keys=True)

#In chuỗi JSON
print("Chuỗi JSON:")
print(json_string)

#In các thành viên đối tượng với mức thụt lề 4
print("\nCác thành viên đối tượng:")
for key, value in python_dict.items():
    print(f"{key}: {value}")
