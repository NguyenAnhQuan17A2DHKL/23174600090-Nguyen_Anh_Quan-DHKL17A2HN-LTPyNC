import numpy as np

#Khởi tạo các mảng:
arr_a = np.array([1,2,3,2,3,4,3,4,5,6])
arr_b = np.array([7,2,10,2,7,4,9,4,9,8])
arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])

#Câu 1: Tìm giao của hai mảng:
arr_c = np.intersect1d(arr_a, arr_b)
print("arr_c:", arr_c)

#Câu 2: Tìm phần tử chỉ xuất hiện ở arr_a:
arr_d = np.setdiff1d(arr_a, arr_b)
print("arr_d:", arr_d)

#Câu 3: Lọc các phần tử trong khoảng từ 5 đến 10 của arr_e:
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]
print("arr_f:", arr_f)