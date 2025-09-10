import numpy as np

# dtype 바꾸기
a = np.arange(5)
print(a)

b = a.astype(np.float64) # 자료형의 스트링을 써도 된다
print(b)

c = np.uint8(a) # dtype 함수를 사용할 수도 있다.
print(c)

# 차원 바꾸기
a = np.arange(6)
print(a)

b = a.reshape(2, 3)
print(b)

c = np.reshape(a, (2, 3))
print(c)

d = np.arange(100).reshape(2, -1)
print(d)

e = np.arange(100).reshape(-1, 5)
print(e)