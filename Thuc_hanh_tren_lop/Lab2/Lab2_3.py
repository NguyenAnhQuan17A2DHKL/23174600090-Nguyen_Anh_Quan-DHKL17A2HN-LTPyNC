import numpy as np

#Định nghĩa hàm đọc dữ liệu:
def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data

#Định nghĩa đường dẫn:
file_path = "C:/Users/SURFACE/Desktop/Uneti/Ki 3/LTPY/Thuc_hanh/Lab2/DATA"
efficiency_file = file_path + "\efficiency.txt"
shifts_file = file_path + "\shifts.txt"

#Đọc dữ liệu:
efficiency = read_data(efficiency_file)
shifts = read_data(shifts_file)

#Bước 2-3: Tạo numpy array và kiểm tra kiểu dữ liệu:
np_shifts = np.array(shifts)
np_efficiency = np.array(efficiency, dtype=int)  #Chuyển đổi về kiểu int để tính toán

print(f"Kiểu dữ liệu của np_shifts: {np_shifts.dtype}")
print(f"Kiểu dữ liệu của np_efficiency: {np_efficiency.dtype}")

#Bước 4-5: Tính hiệu suất trung bình:
morning_efficiency = np_efficiency[np_shifts == 'Morning']
other_shifts_efficiency = np_efficiency[np_shifts != 'Morning']

avg_morning = np.mean(morning_efficiency)
avg_other_shifts = np.mean(other_shifts_efficiency)

print(f"Hiệu suất trung bình của ca sáng: {avg_morning}")
print(f"Hiệu suất trung bình của các ca khác: {avg_other_shifts}")

#Bước 6: Tạo mảng cấu trúc:
workers = np.zeros(len(efficiency), dtype=[('shift', 'U10'), ('efficiency', 'float')])
workers['shift'] = np_shifts
workers['efficiency'] = np_efficiency

#Bước 7: Sắp xếp và tìm ca có hiệu suất cao nhất/thấp nhất:
workers_sorted = np.sort(workers, order='efficiency')

highest_efficiency_shift = workers_sorted[-1]['shift']
lowest_efficiency_shift = workers_sorted[0]['shift']

print(f"Ca có hiệu suất cao nhất: {highest_efficiency_shift}")
print(f"Ca có hiệu suất thấp nhất: {lowest_efficiency_shift}")