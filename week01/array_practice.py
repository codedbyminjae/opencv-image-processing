import numpy as np

# 1. 정수형 배열
a = np.array([1, 2, 3, 4])
print("a:", a)
print("a.dtype:", a.dtype)  # 데이터 타입 확인 (예: int32, int64 등)

# 2. 실수가 섞인 배열
a = np.array([1, 2, 3.14, 4])  # 실수 하나라도 포함되면 전체가 float
print("a:", a)
print("a.dtype:", a.dtype)  # float64 등

# 3. 2행 4열 배열
b = np.array([[1,2,3,4], [5,6,7,8]])
print("b:\n", b)
print("b.shape:", b.shape)  # (2, 4)

# 4. 4행 1열 배열
c = np.array([[1], [2], [3], [4]])
print("c:\n", c)
print("c.shape:", c.shape)  # (4, 1)

# 5. (1, 4) 배열을 만든 후 전치(transpose)
d = np.array([[1, 2, 3, 4]])
print("d:\n", d)
print("d.shape:", d.shape)  # (1, 4)
print("d.T:\n", d.T)
print("d.T.shape:", d.T.shape)  # (4, 1)
