import numpy as np

# 1차원 배열 생성
a = np.arange(12)
print("a =", a)

# vsplit : 수직 분할 (row 방향) → 1차원에서는 split과 동일
# 12개 원소를 3등분 → 각 조각은 길이 4
# print("\nnp.vsplit(a, 3) =", np.vsplit(a, 3))

# 2차원 배열 생성 (4행 3열)
b = np.arange(12).reshape(4, 3)
print("\nb =\n", b)

# vsplit(b,2) : 수직 분할 → 2조각으로 나눔 (2행씩)
print("\nnp.vsplit(b, 2) =", np.vsplit(b, 2))

# split(b,2,0) : axis=0 방향으로 2등분 → vsplit과 동일
print("\nnp.split(b, 2, 0) =", np.split(b, 2, 0))

# vsplit(b,[1]) : 인덱스 1에서 잘라 분할
# 위쪽 0행, 아래쪽 1~3행
print("\nnp.vsplit(b, [1]) =", np.vsplit(b, [1]))

# hsplit(b,[1]) : 인덱스 1에서 잘라 분할 (열 기준)
# 왼쪽 0번째 열, 오른쪽 1~2번째 열
print("\nnp.hsplit(b, [1]) =", np.hsplit(b, [1]))

# split(b,[1],1) : axis=1 방향에서 인덱스 1에서 잘라 분할
# → hsplit과 동일
print("\nnp.split(b, [1], 1) =", np.split(b, [1], 1))
