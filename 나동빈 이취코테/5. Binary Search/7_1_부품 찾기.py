# 문제 : 정수 형태의 고유한 번호가 있는 N개의 부품이 있고, 손님이 M개 종류의 부품의 존재 유무를 확인 요청했을 때, 가게 안에 부품이 있는지 확인하여 출력하기
#       손님이 요청한 부품 번호의 순서대로 부품을 확인하여, 있으면 'yes'를, 없으면 'no'를 공백으로 구분하여 출력
# 조건 : 1 <= N <= 1,000,000 / 1 <= M <= 100,000 / 1 <= 고유 번호(정수) 값의 범위 <= 1,000,000

##### 내 풀이
# 아이디어 : 데이터가 최대 1백만 개까지 주어질 수 있으므로 sys.stdin.readline()으로 input data 가져오기
#          전체 데이터 정렬 후, 재귀 함수로 구현한 이진 탐색 함수의 target 값만 바꿔주며 부품의 존재 유무를 "yes", "no"로 출력
# 참고 : (1) 반복문 안에서 함수를 적용하여 각 target의 결과를 구하고 비교해서 출력하는 것보다 (2) map 함수를 적용해서 결과값을 모두 구한 뒤 결과를 비교해서 출력하는 것이 더 빠름
import sys

n = int(sys.stdin.readline())
total = list(map(int, sys.stdin.readline().strip().split()))
total.sort()

m = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().strip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# (1) 반복문 안에서 함수를 적용하여 각 target의 결과를 구하고 비교해서 출력
# for i in range(len(request)):
#     result = binary_search(total, request[i], 0, n - 1)
#     if result == True:
#         print("yes", end = ' ')
#     else:
#         print("no", end = ' ')

# (2) map 함수를 적용해서 결과값을 모두 구한 뒤 결과를 비교해서 출력
result = list(map(lambda i: binary_search(total, i, 0, n - 1), request))
for r in result:
    if r == True:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')


##### 답안 예시 1 (이진 탐색) : 다량의 데이터 검색은 이진 탐색 알고리즘을 이용해 효과적으로 처리할 수 있음
# 전체 시간복잡도 : O((M + N) x logN)
# 1. 먼저 매장 내 N개의 부품을 번호를 기준으로 정렬
#    -> N개의 부품을 정렬하는 과정에서, 요구되는 시간 복잡도 O(N x logN)
#    -> 즉, 이론상 최대 약 2,000만 번의 연산이 필요
#    -> (cf) log2(1,000,000) = 약 20
# 2. M개의 찾고자 하는 부품이 각각 매장에 존재하는지 검사
#    -> M개의 부품을 찾는 과정에서, 최악의 경우 시간 복잡도 O(M x logN)의 연산이 필요
#    -> 즉, 이론상 최대 약 200만 번의 연산이 이루어짐
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 index 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인
        else:
            start = mid + 1
    return None

n = int(input())                          # N(가게의 부품 개수) 입력
array = list(map(int, input().split()))   # 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array.sort()                              # 이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input())                          # M(손님이 확인 요청한 부품 개수) 입력
x = list(map(int, input().split()))       # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n - 1)    # 해당 부품이 존재하는지 확인
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


##### 답안 예시 2 (계수 정렬)
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤, 리스트의 index에 직접 접근하여 특정 번호의 부품이 매장에 존재하는지 확인
n = int(input())           # N(가게의 부품 개수) 입력받기
array = [0] * 1000001      # 부품의 고유 번호 최댓값이 1,000,000이므로

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수) 입력받기
m = int(input())
x = list(map(int, input().split()))    # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


##### 답안 예시 3 (집합 자료형 이용)
# 집합(set) 자료형 : 단순히 특정 데이터가 존재하는지 검사할 때 효과적으로 사용할 수 있음
# 코드의 간결성 측면에서 가장 우수함
n = int(input())                         # N(가게의 부품 개수) 입력받기
array = set(map(int, input().split()))   # 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록

# M(손님이 확인 요청한 부품 개수) 입력받기
m = int(input())
x = list(map(int, input().split()))      # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


# Test Case.
# < input >
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# output : no yes yes