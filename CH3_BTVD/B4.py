import numpy as np

#Bài 1: Tạo arr_zeros có 10 phần tử 0, cập nhật phần tử ở vị trí thứ 5 là 1:
arr_zeros = np.zeros(10)
arr_zeros[4] = 1  # Vì index bắt đầu từ 0 nên vị trí thứ 5 có index là 4:

#Bài 2: Tạo arr_h có giá trị từ 10 đến 24. In danh sách các phần tử theo thứ tự đảo ngược:
arr_h = np.arange(10, 25)
print(arr_h[::-1])  #Đảo ngược mảng

#Bài 3: Cho arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0]), tạo arr_l từ arr_k với các phần tử khác 0:
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_l = arr_k[arr_k != 0]  #Lọc các phần tử khác 0

#Bài 4: Từ arr_l của câu 3, thêm 2 phần tử có giá trị là 10 và 20 vào cuối array:
arr_l = np.append(arr_l, [10, 20])

#Bài 5: Từ array của câu 4, thêm phần tử có giá trị 100 vào vị trí có index = 5:
arr_l = np.insert(arr_l, 5, 100)

#Bài 6: Từ array của câu 5, xóa các phần tử tại vị trí có index = 0, 1, 2:
arr_l = np.delete(arr_l, [0, 1, 2])

print(arr_l)