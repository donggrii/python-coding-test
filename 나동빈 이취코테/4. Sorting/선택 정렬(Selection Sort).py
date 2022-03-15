# 선택 정렬(Selection Sort) : 매번 '가장 작은 것을 선택'하여 앞으로 보내는 과정을 (N - 1)번 반복하여 정렬
# 시간 복잡도(= O(N^2)) : (N - 1)번만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 하므로 매번 '비교 연산'이 필요함
#                      (N + (N - 1) + (N - 2) + ... + 2) -> (N x (N + 1) / 2) = (N^2 + N) / 2 -> O(N^2)
# 효율성 : 데이터의 개수가 10,000개 이상이면 정렬 속도가 급격히 느려짐
#        기본 정렬 라이브러리(내부적으로 C 언어 기반, 다양한 최적화 테크닉이 포함됨)를 포함해 다른 정렬 알고리즘에 비해 매우 비효율적
# 장점 : 특정한 리스트에서 가장 작은 데이터를 찾는 일이 코딩 테스트에 자주 등장하므로 선택 정렬 소스코드에 익숙해질 필요 있음

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i     # 가장 작은 원소의 index
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]   # swap

print(array)
