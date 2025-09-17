import numpy as np

# ==========================================================
# 2.9 검색 기능 (numpy.where, nonzero, stack)
# 조건에 맞는 요소의 값 / 인덱스를 반환하는 기능
# ==========================================================

# 예제 1: 기본 where 사용
a = np.arange(12).reshape(3, 4)
print("a =\n", a)

# 조건에 맞는 인덱스 구하기 (a > 6)
coords = np.where(a > 6)
print("\n조건 (a>6)에 맞는 인덱스 coords =", coords)

# 인덱스를 행렬 좌표쌍으로 보기 좋게 stack
print("\nstack으로 좌표쌍 정리 =\n", np.stack((coords[0], coords[1]), -1))

# ==========================================================
# 예제 2: np.nonzero() → 0이 아닌 값들의 인덱스 반환
# ==========================================================
b = np.array([0, 1, 2, 0, 2, 1, 2])
print("\nb =", b)

nonzero_idx = np.nonzero(b)
print("np.nonzero(b) =", nonzero_idx)   # 0이 아닌 값들의 위치

# ==========================================================
# 예제 3: 다차원 배열에서 nonzero()
# ==========================================================
c = np.array([[0, 1, 2],
              [1, 2, 0],
              [2, 0, 1]])
print("\nc =\n", c)

coords_c = np.nonzero(c)
print("np.nonzero(c) =", coords_c)

print("stack으로 좌표쌍 정리 =\n", np.stack((coords_c[0], coords_c[1]), -1))
