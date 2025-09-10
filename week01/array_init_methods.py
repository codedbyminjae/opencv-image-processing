import numpy as np

# 1. 빈 배열 만들기 (초기화되지 않은 값이 채워짐 - 예측 불가한 쓰레기 값)
a = np.empty((2, 3))
print("a (empty):\n", a)
print("a.dtype:", a.dtype)

# fill()로 직접 값 채우기
a.fill(255)
print("a after fill(255):\n", a)

# 2. 0으로 채워진 배열 만들기
b = np.zeros((2, 3))
print("b (zeros):\n", b)

# 3. 0으로 채우되 dtype을 np.uint8로 지정 (이미지 픽셀용 정수 8비트)
c = np.zeros((2, 3), dtype=np.uint8)
print("c (zeros, uint8):\n", c)

# 4. 1로 채워진 배열 만들기
d = np.ones((2, 3), dtype=np.int16)
print("d (ones, int16):\n", d)

# 5. full()로 배열 생성과 동시에 값 채우기 (여기선 255로 채움)
e = np.full((2, 4, 3), 255, dtype=np.uint8)  # 2행 4열, 3채널(RGB)
print("e (full, 255 RGB):\n", e)
