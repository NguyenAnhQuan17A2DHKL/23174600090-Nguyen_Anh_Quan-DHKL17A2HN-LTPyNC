import json

# Dữ liệu JSON mẫu
json_data = '''
{
    "company": {
        "name": "Công ty TNHH Đất Việt",
        "address": "abc Giải Phóng – Hà Nội",
        "employees": [
            {"name": "Nguyễn Văn A", "unit": "Đơn vị A1"},
            {"name": "Trần Thị B", "unit": "Đơn vị A2"},
            {"name": "Lê Văn C", "unit": "Đơn vị A1"},
            {"name": "Phạm Thị D", "unit": "Đơn vị A3"},
            {"name": "Hoàng Văn E", "unit": "Đơn vị A2"},
            {"name": "Ngô Thị F", "unit": "Đơn vị A4"},
            {"name": "Đặng Văn G", "unit": "Đơn vị A4"},
            {"name": "Bùi Thị H", "unit": "Đơn vị A3"}
        ]
    }
}
'''

# Chuyển đổi JSON thành đối tượng Python
data = json.loads(json_data)

# Lấy thông tin công ty
company_name = data["company"]["name"]
company_address = data["company"]["address"]
employees = data["company"]["employees"]

# Tính tổng số nhân viên
total_employees = len(employees)

# Thống kê nhân viên theo đơn vị
unit_stats = {}
for employee in employees:
    unit = employee["unit"]
    if unit not in unit_stats:
        unit_stats[unit] = 0
    unit_stats[unit] += 1

# In thông tin công ty và thống kê nhân viên
print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {company_address}")
print(f"Tổng số nhân viên: {total_employees}")
print("-----Thống kê nhân viên theo đơn vị------")

for i, (unit, count) in enumerate(unit_stats.items(), 1):
    percentage = (count / total_employees) * 100
    print(f"{i}./Tên đơn vị: {unit}.")
    print(f"- Số nhân viên: {count}")
    print(f"- Tỷ lệ: {percentage:.2f}%")
