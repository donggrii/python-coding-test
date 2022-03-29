# 이진 탐색(Binary Search) : 위치를 나타내는 변수 3개(시작점, 끝점, 중간점)를 이용하여, 찾으려는 데이터(target)와 중간점 위치에 있는 데이터(middle)를 반복적으로 비교해서 원하는 데이터를 탐색
# 과정 : 1. 시작점(start)과 끝점(end)을 확인하고 둘 사이의 중간점(mid)을 정함 (중간점이 실수일 때는 소수점 이하를 버림)
#       2. 중간점의 데이터(mid)와 찾으려는 데이터(target)를 비교
#           a. 중간점(mid)과 찾으려는 데이터(target)가 동일하면 탐색을 종료
#           b. 중간점(mid)이 더 크면, 끝점(end)을 (mid - 1)로 옮기고 왼쪽을 탐색
#           c. 중간점(mid)이 더 작으면, 시작점(start)을 (mid + 1)로 옮기고 오른쪽을 탐색
# 특징 : 배열 내부의 데이터가 '정렬'되어 있어야만 사용할 수 있는 알고리즘 
#       -> 데이터가 random할 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있음
# 시간 복잡도(= O(logN)) : 한 번 확인할 때마다 확인하는 원소의 개수가 '평균적으로' 절반씩 줄어들기 때문 (= 탐색 범위를 절반씩 좁혀가며 데이터를 탐색)
#                       -> 단계마다 2로 나누는 것과 동일하므로 연산횟수가 log2(n)에 비례
# 출제 유형 : 높은 난이도의 문제에서는 이진 탐색 알고리즘이 다른 알고리즘과 함께 사용되기도 함 (ex. 그리디 + 이진 탐색)
#           보통 '탐색 범위가 큰 상황'에서의 탐색을 가정하는 경우가 많음
#           -> "탐색 범위가 2,000만을 넘어가면" 이진 탐색으로 접근해볼 것
#           -> "처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면" 이진 탐색과 같이 O(logN)의 속도를 내야 하는 알고리즘을 떠올려야 함

# 재귀 함수로 구현한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # 찾은 경우 중간점 index 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# 반복문으로 구현한 이진 탐색
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

n, target = list(map(int, input().split()))   # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
array = list(map(int, input().split()))       # 전체 원소 입력받기

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    
# Test Case 1.
# < input >
# 10 7
# 1 3 5 7 9 11 13 15 17 19

# output : 4

# Test Case 2.
# < input >
# 10 7
# 1 3 5 6 9 11 13 15 17 19

# output : "원소가 존재하지 않습니다."