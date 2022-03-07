# '선택 정렬'과 '기본 정렬 라이브러리'의 수행 시간 비교
from random import randint
import time

##### 선택 정렬 : 최악의 경우 시간 복잡도가 O(N^2)
# 배열에 10,000개의 정수 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))   # 1부터 100 사이의 랜덤한 정수
    
start_time = time.time()

for i in range(len(array) - 1):
    min_index = i       # 가장 작은 원소의 index
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()

print("선택 정렬 성능 측정:", end_time - start_time)            # 선택 정렬 성능 측정: 6.180602788925171

##### 기본 정렬 라이브러리 : 최악의 경우 시간 복잡도가 O(NlogN)
# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))   # 1부터 100 사이의 랜덤한 정수

start_time = time.time()

array.sort()    # 기본 정렬 라이브러리 사용

end_time = time.time()

print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)   # 기본 정렬 라이브러리 성능 측정: 0.0008940696716308594