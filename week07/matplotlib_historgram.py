import numpy as np, cv2
import matplotlib.pyplot as plt

# 1️⃣ 이미지 읽기
image = cv2.imread("images/draw_hist.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("이미지를 찾을 수 없습니다!")

# 2️⃣ 히스토그램 계산 (NumPy 사용)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])  # OpenCV 내장 함수

# 3️⃣ Matplotlib으로 히스토그램 시각화
plt.figure(figsize=(8, 4))
plt.title('Gray-Level Histogram')
plt.xlabel('Pixel Value (0~255)')
plt.ylabel('Number of Pixels')
plt.plot(hist, color='gray')
plt.xlim([0, 256])
plt.grid(alpha=0.3)
plt.show()
