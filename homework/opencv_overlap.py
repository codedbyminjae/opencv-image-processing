import numpy as np, cv2

# 이미지 불러오기
image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR) # 원본 영상 읽기
logo  = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR) # 로고 영상 읽기

if image is None or logo is None: raise Exception("영상파일 읽기 오류") # 이미지 읽기 오류시 예외 처리

# 로고에서 전경과 배경을 분리하기위한 마스크 생성
masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1] # 로고 영상 이진화
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)   # 전경 통과 마스크
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)            # 배경 통과 마스크

# 이미지와 로고 크기 정보 추출
(H, W), (h, w) = image.shape[:2], logo.shape[:2] # 전체 영상, 로고 영상 크기

# 마우스 클릭 콜백 함수
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 좌클릭시 이미지 생성
        temp = image.copy()  # 이전 로고 제거 효과

        x1, y1, = x, y
        x2, y2 = x + w, y + h

        # 배경 이미지 중 합성할 영역을 roi로 지정
        roi = temp[y1:y2, x1:x2]

        # 만약 ROI가 로고보다 작은 경우 (즉, 경계에 걸린 경우)
        if roi.shape[0] < h or roi.shape[1] < w:
            # ROI 크기에 맞게 로고와 마스크를 잘라서 사용
            logo_cut = logo[:roi.shape[0], :roi.shape[1]]
            fg_mask_cut = fg_pass_mask[:roi.shape[0], :roi.shape[1]]
            bg_mask_cut = bg_pass_mask[:roi.shape[0], :roi.shape[1]]
            
            # 전경만 통과시키고, 배경은 ROI 원본 유지
            foreground = cv2.bitwise_and(logo_cut, logo_cut, mask=fg_mask_cut)
            background = cv2.bitwise_and(roi, roi, mask=bg_mask_cut)
            dst = cv2.add(background, foreground) # 합성

        else:
            # 정상 범위인 경우
            foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
            background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

            dst = cv2.add(background, foreground)
        
        # 합성 결과 원본 이미지에 덮어쓰기
        temp[y:y + h, x:x + w] = dst

        cv2.imshow("image", temp)

cv2.imshow("image", image)
cv2.setMouseCallback("image", on_mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
