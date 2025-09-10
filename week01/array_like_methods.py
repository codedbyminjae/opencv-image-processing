import cv2
import numpy as np

# 1. 원본 이미지 불러오기 (배열로 읽힘)
img = cv2.imread('images/read_color.jpg')
print("원본 이미지 shape:", img.shape)

# 2. 동일한 크기의 빈 배열 만들기 (초기화 안 됨 → 쓰레기값)
a = np.empty_like(img)
print("a (empty_like) shape:", a.shape)

# 3. 동일한 크기의 배열 만들기 (모든 값 0 → 검정 이미지용)
b = np.zeros_like(img)
print("b (zeros_like) shape:", b.shape)

# 4. shape 비교
print("img.shape == a.shape?", img.shape == a.shape)
print("img.shape == b.shape?", img.shape == b.shape)
