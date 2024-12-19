import numpy as np

#1. Tạo mảng arr và hiển thị thông tin:
arr = np.arange(10)  #Tạo mảng từ 0 đến 9
print("Mảng arr:", arr)
print("Kiểu dữ liệu:", arr.dtype)
print("Kích thước:", arr.shape)

#2. Tạo mảng các số lẻ và số chẵn:
arr_odd = arr[arr % 2 == 1]  #Lọc các số lẻ:
arr_even = arr[arr % 2 == 0]  #Lọc các số chẵn:
print("Mảng các số lẻ:", arr_odd)
print("Mảng các số chẵn:", arr_even)

#:3. Tạo mảng arr_update_1
arr_update_1 = np.where(arr % 2 == 1, 100, arr)  #Thay thế các số lẻ bằng 100:
print("Mảng arr_update_1:", arr_update_1)