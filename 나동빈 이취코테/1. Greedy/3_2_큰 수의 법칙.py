# 문제 : 주어진 수 M번 더하여 가장 큰 수 만들기(특정 인덱스에 해당하는 수를 연속으로 K번까지만 더할 수 있음)

# 내 풀이
# 아이디어 : 가장 큰 수를 K번 더하고 두번째로 큰 수를 1번 더하고 다시 가장 큰 수를 K번 더하는 것 반복
n, m, k = 5, 8, 3
lst = [2, 4, 5, 4, 6]
answer = 0
lst.sort(reverse=True)
nums = lst[0], lst[1]

while m > 0:
    if m - k > 0:
        answer += k * nums[0]
        m -= k
        if m - 1 >= 0:
            answer += nums[1]
            m -= 1
    else:
        answer += m * nums[0]
        break
print(answer)   # 46

# 단순하게 푸는 답안 예시
n, m, k = map(int, input().split())      # N, M, K를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))   # N개의 수를 공백으로 구분하여 입력받기
data.sort()            # 입력받은 수들 정렬하기
first = data[n - 1]    # 가장 큰 수
second = data[n - 2]   # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):    # 가장 큰 수를 K번 더하기
        if m == 0:        # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1            # 더할 때마다 1씩 빼기
    if m == 0:            # m이 0이라면 반복문 탈출
        break
    result += second      # 두 번째로 큰 수를 1번 더하기
    m -= 1                # 더할 때마다 1씩 빼기
    
print(result)  # 최종 답안 출력

# 간단한 수학적 아이디어(반복되는 수열)를 이용해 더 효율적으로 푸는 답안 예시
# < 아이디어 >
# 가장 큰 수와 두 번째로 큰 수가 "특정한 수열 형태로 일정하게 반복해서 더해지는 특징"이 있으므로
# 가장 큰 수가 더해지는 횟수를 구하고, 이를 이용해 두 번째로 큰 수가 더해지는 횟수를 구해서 각각 곱해주는 것
# 즉, 가장 큰 수가 더해지는 횟수 : int(M / (K + 1)) * K + M % (K + 1)
n, m, k = map(int, input().split())      # N, M, K를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))   # N개의 수를 공백으로 구분하여 입력받기
data.sort()            # 입력받은 수들 정렬하기
first = data[n - 1]    # 가장 큰 수
second = data[n - 2]   # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first       # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)   # 최종 답안 출력


# Test Case 1.
# n, m, k = 5, 8, 3
# data = [2, 4, 5, 4, 6]
# return : 46 (6*3 + 5*1 + 6*3 + 5*1)

# Test Case 2.
# n, m, k = 5, 7, 2
# data = [3, 4, 3, 4, 3]
# return : 28 (4*2 + 4*1 + 4*2 + 4*1 + 4*1)

# Test Case 3.
# n, m, k = 5, 8, 4
# data = [2, 4, 5, 4, 6]
# return : 47 (6*4 + 5*1 + 6*3)