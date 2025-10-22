import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("Images not found")
print('image1:', image1.dtype)

# 영상 합성
alpha, beta = 0.6, 0.7 # 곱셈 비율
add_img1 = cv2.add(image1, image2) # 두 영상 단순 더하기
print('add_img1:', add_img1.dtype)
add_img2 = cv2.add(add_img1 * alpha, image2 * beta) # 두 영상 비율에 따른 더하기
print('add_img2:', add_img2.dtype)
add_img2 = np.clip(add_img2, 0, 255).astype("uint8") # saturation 처리
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0) # 두 영상 비율에 따른 더하기
print('add_img3:', add_img3.dtype)

titles = ['image1', 'image2', 'add_img1', 'add_img2', 'add_img3']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)
cv2.destroyAllWindows()