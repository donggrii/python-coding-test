# 내 풀이
# 1번째 행의 최소값을 result에 담고, 반복문으로 2번째 행부터 마지막 행까지 각각의 최소값과 result를 비교해서 각 행의 최소값이 result보다 크면 그 값을 result로 업데이트하면서 가장 큰 수를 찾기
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = min(data[0])
for i in range(1, n):
    minimum = min(data[i])
    result = minimum if result < minimum else result
print(result)

# min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())     # N, M을 공백으로 구분하여 입력받기

result = 0
for i in range(n):                   # 한 줄씩 입력받아 확인
    data = list(map(int, input().split()))
    min_value = min(data)            # 현재 줄에서 '가장 작은 수' 찾기
    result = max(result, min_value)  # '가장 작은 수'들 중에서 가장 큰 수 찾기
print(result)   # 최종 답안 출력

# 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())     # N, M을 공백으로 구분하여 입력받기

result = 0
for i in range(n):                   # 한 줄씩 입력받아 확인
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)  # '가장 작은 수'들 중에서 가장 큰 수 찾기
print(result)   # 최종 답안 출력


# Test Case 1.
# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# return : 2

# Test Case 2.
# 입력 예시
# 2 4
# 7 3 1 8
# 3 3 3 4
# return : 3