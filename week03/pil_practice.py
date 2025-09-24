import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# img = cv2.imread("images/je.jpg")
img = np.zeros((300, 500, 3), dtype=np.uint8)
img = Image.fromarray(img)
font = ImageFont.truetype('gulim.ttc', 50)
# font = ImageFont.truetype('NanumGothicLight.ttf', 30)
draw = ImageDraw.Draw(img)
draw.text((100, 100), '안녕하세요. 한글~', font=font, fill=(255, 255, 0), stroke_width=1)

img = np.array(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
