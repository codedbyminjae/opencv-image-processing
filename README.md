# 🎥 영상처리 프로그래밍 (Python + OpenCV)

> 이 저장소는 **영상처리 프로그래밍** 과목 실습을 정리한 공간입니다.  
> 현재는 **기초 Python 프로그래밍**을 학습하고 있으며, 추후 **OpenCV**를 활용한 영상처리 프로그래밍을 진행할 예정입니다.

---

## 📌 학습 목표
- Python 기본 문법 및 Numpy 활용 능력 강화
- 배열, 인덱싱, 브로드캐스팅, 슬라이싱 실습
- OpenCV 라이브러리를 이용한 영상 처리
- 실습 코드와 주석을 정리하여 기록

---

## 🗂️ 주차별 진행
- **Week 01 ~ 02**: Python 기초, Numpy 배열 다루기  
- **Week 03 ~ 04**: Numpy 고급 기능 (split, stack, 조건 검색 등)  
- **Week 05 이후**: OpenCV 기초 및 영상 처리 응용  

---

## 🛠️ 사용 기술
- **Language**: Python 3.x  
- **Libraries**:  
  - [Numpy](https://numpy.org/)  
  - [OpenCV](https://opencv.org/) (예정)

---

## 📖 예시 코드

```python
import numpy as np
import cv2   # 추후 실습에서 활용 예정

# 간단한 numpy 배열 예제
a = np.arange(12).reshape(3, 4)
print("배열 a =\n", a)
