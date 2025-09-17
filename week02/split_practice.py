import numpy as np

# 1차원 배열 생성 (0 ~ 11)
a = np.arange(12)
print("a =", a)

# 배열을 3등분 (12개 원소 → 4개씩 나눔)
z = np.hsplit(a, 3)
print("np.hsplit(a, 3) =", z)

# 인덱스 3, 6 기준으로 자르기
# [0~2], [3~5], [6~11] 세 구간으로 나뉨
x = np.hsplit(a, (3, 6))
print("np.hsplit(a, (3,6)) =", x)

# np.split : 지정한 개수만큼 나눔
# 0번 축(axis=0)을 따라 3등분 → [0~3], [4~7], [8~11]
c = np.split(a, 3, 0)
print("np.split(a, 3, 0) =", c)

# 인덱스 [3,6,9] 기준으로 나누기
# [0~2], [3~5], [6~8], [9~11]
v = np.split(a, [3, 6, 9], 0)
print("np.split(a, [3,6,9], 0) =", v)

# vsplit이 가능하기 위해서는 2개 이상의 차원이 필요하다
