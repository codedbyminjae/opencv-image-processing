import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

# 행 별로 출력
print(a[0])
print(a[1])
# 2행 3열
print(a[2,3])

# 0행~1행, 1열~2열
b = a[0:2, 1:3]
print(b)

# 부분 정리 가능
b[0] = 99
print(b)

print(a)