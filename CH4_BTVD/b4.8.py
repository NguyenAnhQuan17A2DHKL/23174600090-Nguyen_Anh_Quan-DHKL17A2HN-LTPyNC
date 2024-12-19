import pandas as pd
import numpy as np

ser = pd.Series(np.random.random(20))

ser_quantiles = pd.qcut(ser, q=10, labels=[f"Decile {i+1}" for i in range(10)])

print("Dữ liệu ban đầu:")
print(ser)
print("\nDữ liệu sau khi thay thế bằng tên phân vị:")
print(ser_quantiles)