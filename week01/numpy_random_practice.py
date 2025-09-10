import numpy as np

# 시퀀스 생성
a = np.arange(5)
print("a:", a)

b = np.arange(5.0)
print("b:", b)

c = np.arange(3, 9, 2)  # 시작, 끝, 증분
print("c:", c)

# 난수 생성
d = np.random.rand(2, 3)  # 0~1 사이값으로 2행 3열
print("d:\n", d)

e = np.random.randn(2, 3)  # 표준정규분포 (평균 0, 분산 1)
print("e:\n", e)

f = np.random.randint(0, 256, (3, 3))  # 시작, 끝(미포함), 3행 3열 정수 랜덤
print("f:\n", f)
