# 문제 : N개의 자연수로 구성된 두 개의 배열 A, B가 있을 때, A의 원소와 B의 원소를 최대 K번 바꿔치기하여 A의 모든 원소의 합이 최대가 되도록 출력하기 (1 <= N <= 100,000, 0 <= K <= N)
#       => 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 함!

##### 내 풀이
# 아이디어 : A를 오름차순 정렬, B를 내림차순 정렬하여 (K-1)번째 원소까지 매번 두 배열의 원소를 비교하며 교체
#          '최대' K번 연산이므로 A와 B의 원소를 바꾸기 전, 값을 비교하여 A[i] <= B[i]인지 확인
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)
for i in range(k):
    if A[i] <= B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))    # A의 모든 원소 합 출력

##### 답안 예시
# 아이디어 : 매번 A에서 가장 작은 원소를 골라서, B에서 가장 큰 원소와 교체하기
#          단, A에서 가장 작은 원소가 B에서 가장 큰 원소보다 작을 때에만 교체를 수행 (K번 반복)
n, k = map(int, input().split())       # N과 K를 입력받기
a = list(map(int, input().split()))    # 배열 A의 모든 원소 입력받기
b = list(map(int, input().split()))    # 배열 B의 모든 원소 입력받기

a.sort()                  # 배열 A는 오름차순 정렬
b.sort(reverse = True)    # 배열 B는 내림차순 정렬

# 첫 번째 index부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    if a[i] < b[i]:              # A의 원소가 B의 원소보다 작은 경우
        a[i], b[i] = b[i], a[i]  # 두 원소를 교체
    else:                        # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))   # 배열 A의 모든 원소의 합을 출력


# Test Case.
# < input >
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

# output : 26