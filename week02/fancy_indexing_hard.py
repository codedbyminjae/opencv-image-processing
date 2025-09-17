import numpy as np

# 3차원 배열 생성 (shape: (2,5,3))
# 첫 번째 축: 2개, 두 번째 축: 5개, 세 번째 축: 3개
b = np.arange(30).reshape(2, 5, 3)
print("b =\n", b)

# Fancy Indexing 예제
# 첫 번째 축 인덱스: [0,1,0,0,1] → 총 5개 선택
# 두 번째 축 인덱스: np.arange(5) → [0,1,2,3,4]
# 세 번째 축 인덱스: np.random.randint(0,3,(5,)) → [0~2 사이 정수 5개 랜덤]
# 따라서 총 5개의 (i,j,k) 좌표를 만들어 b[i,j,k] 값 추출
result = b[[0, 1, 0, 0, 1], np.arange(5), np.random.randint(0, 3, (5,))]

print("result =", result)  # 실행할 때마다 달라짐 (랜덤)
