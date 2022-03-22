# 문제 : 수열을 내림차순으로 정렬하기 (1 <= N <= 500, 수의 범위는 1 이상 100,000 이하의 자연수)
# 출력 조건 : 내림차순으로 정렬된 결과를 공백으로 구분하여 출력. 동일한 수의 순서는 자유롭게 출력해도 됨.

##### 내 풀이 1
# 아이디어 : 파이썬 기본 정렬 라이브러리 내림차순 정렬
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse = True)
for i in range(len(nums)):
    print(nums[i], end = ' ')

##### 내 풀이 2
# 아이디어 : 특정 조건(큰 수와 작은 수의 차이가 1,000,000 이하, 모든 수는 자연수)을 만족하므로 계수 정렬을 이용해 더 빠르게 정렬
n = int(input())
nums = [int(input()) for _ in range(n)]
count = [0] * (max(nums) + 1)

for i in range(len(nums)):
    count[nums[i]] += 1

for i in range(len(count) - 1, 0, -1):
    for j in range(count[i]):
        print(i, end = ' ')

##### 답안 예시
n = int(input())    # N을 입력받기

array = []
for i in range(n):  # N개의 정수를 입력받아 리스트에 저장
    array.append(int(input()))

array = sorted(array, reverse = True)   # 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행

# 정렬이 수행된 결과 출력
for i in array:
    print(i, end = ' ')


# Test Case.
# < input >
# 3
# 15
# 27
# 12

# output : 27 15 12