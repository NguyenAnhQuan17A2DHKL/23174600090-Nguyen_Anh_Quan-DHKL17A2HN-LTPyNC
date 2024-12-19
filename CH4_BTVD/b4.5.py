import pandas as pd
import numpy as np

#Tạo Series ngẫu nhiên:
ser = pd.Series(np.random.normal(10, 5, 25))

#1. Giá trị tối thiểu:
min_value = ser.min()

#2. Phần centile thứ 25:
percentile_25 = ser.quantile(0.25)

#3. Trung vị:
median_value = ser.median()

#4. Phần centile thứ 75:
percentile_75 = ser.quantile(0.75)

#5. Giá trị tối đa:
max_value = ser.max()

#In kết quả:
print(f"Giá trị tối thiểu (min): {min_value}")
print(f"Phần centile thứ 25 (25th percentile): {percentile_25}")
print(f"Trung vị (median): {median_value}")
print(f"Phần centile thứ 75 (75th percentile): {percentile_75}")
print(f"Giá trị tối đa (max): {max_value}")