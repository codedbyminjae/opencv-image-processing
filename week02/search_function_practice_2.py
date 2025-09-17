import numpy as np

# ==========================================================
# np.all / np.any
# 배열의 특정 축(axis) 방향으로 모든 값이 True인지,
# 혹은 하나라도 True가 있는지를 검사하는 함수
# ==========================================================

# 예제 1: 3차원 불리언 배열 생성
d = np.array([[[True, False, True, True],
               [True, True, False, True],
               [True, True, True, True]],
              [[True, True, True, True],
               [True, False, True, True],
               [False, True, True, True]]])

print("d.shape =", d.shape)  # (2, 3, 4)

# 축 0 기준: 각 위치(3x4)에 대해 두 '층' 모두 True인지 확인
print("\nnp.all(d, 0) =\n", np.all(d, 0))

# 축 1 기준: 각 위치(2x4)에 대해 3행 모두 True인지 확인
print("\nnp.all(d, 1) =\n", np.all(d, 1))

# 축 2 기준: 각 위치(2x3)에 대해 4열 모두 True인지 확인
print("\nnp.all(d, 2) =\n", np.all(d, 2))

# ==========================================================
# 예제 2: 두 배열 비교
# ==========================================================
a = np.arange(10)
b = np.arange(10)
print("\na =", a)
print("b =", b)

# 두 배열이 같은지 비교
print("\na == b =", a == b)

# 모든 원소가 같다면 True
print("np.all(a == b) =", np.all(a == b))

# b 배열의 원소 하나 변경
b[5] = -1
print("\n변경된 b =", b)

# 다시 비교 → 하나라도 다르므로 False
print("np.all(a == b) =", np.all(a == b))

# ==========================================================
# 예제 3: np.any
# ==========================================================
# any는 '하나라도 True이면 True'
print("\nnp.any(d) =", np.any(d))  # d 전체에 True가 하나라도 있으면 True
print("np.any(a == b) =", np.any(a == b))  # 일부 원소라도 같으면 True
