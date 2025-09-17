import numpy as np

a = np.arange(3, 8)
print(a)

b = [1, 2, 3]
print(a[b])

mask = np.array([True, False, True, False, True])
print(a[mask])

a = np.arange(10)
print(a)

b = a >= 5
print(b)
print(a[b])

# 원하는 위치에 특정한 값을 할당하는 방법으로 많이 사용한다.
a[a > 5] = 1
print(a)

# 2차원 배열 예제
a = np.arange(30).reshape(5, 6)
print(a)

print(a[[3], [5]])
print(a[[0,2], [2, 3]])

# 3차원 배열 예제
b = np.arange(30).reshape(2, 5, 3)
print(b)

print("b[[0,1],[2,3],[1,2]] =", b[[0,1], [2,3], [1,2]])