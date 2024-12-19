'''
+) list('abcdefgh'): Tạo danh sách các ký tự ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].
+) np.random.randint(8, size=30): Tạo một mảng numpy gồm 30 số ngẫu nhiên trong khoảng từ 0 đến 7 (giá trị bắt đầu từ 0 và nhỏ hơn 8).
+) np.take(list('abcdefgh'), ...): Lấy các phần tử từ danh sách ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] dựa trên các chỉ số ngẫu nhiên được tạo bởi np.random.randint.
'''

#2. Tính số lần xuất hiện của mỗi giá trị duy nhất trong ser:
import pandas as pd
import numpy as np

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
value_counts = ser.value_counts()

print("Số lần xuất hiện của mỗi giá trị duy nhất:")
print(value_counts)

