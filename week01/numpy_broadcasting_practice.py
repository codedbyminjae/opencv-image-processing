import numpy as np

# 2.5.1 Numpy 배열과 스칼라값 연산
a = np.arange(5)
print("a =", a)
print("a + 5 =", a + 5)

b = np.arange(6).reshape(2, -1)
print("b =\n", b)
print("b + 2 =\n", b + 2)  # 브로드캐스팅 가능

# 2.5.2 배열간의 브로드캐스팅 규칙
a = np.arange(24).reshape(2, 3, 4)
b = np.arange(12).reshape(3, 4)
print("a =\n", a)
print("b =\n", b)
print("a + b =\n", a + b)

# 규칙 위반 예시
a = np.arange(6).reshape(3, 1)
c = np.arange(6)
print("a + c =\n", a + c)

d = np.arange(6).reshape(2, 3, 1)
e = np.arange(6).reshape(2, 1, 3)
# print(d + e)  # 오류 발생: 브로드캐스팅 불가

f = np.arange(6).reshape(2, 3, 1)
g = np.arange(2).reshape(2, 1, 1)
print("f + g =\n", f + g)
