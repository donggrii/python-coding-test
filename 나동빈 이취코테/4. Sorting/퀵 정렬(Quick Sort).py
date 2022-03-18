# 퀵 정렬(Quick Sort) : 기준 데이터(pivot)를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼 후 리스트를 반으로 나누는 방식으로 정렬
# Part 1 (Divide, Partition) : 리스트의 1번째 데이터를 pivot으로 설정한 뒤, 왼쪽에서부터 pivot보다 큰 데이터를 찾고, 오른쪽에서부터 pivot보다 작은 데이터를 찾아 위치를 서로 교환해주는 과정 반복
#                              -> 왼쪽에서부터 찾는 값과 오른쪽에서부터 찾는 값의 위치가 엇갈릴 경우 '작은 데이터'와 'pivot'의 위치를 서로 변경
#                              -> pivot의 왼쪽에는 pivot보다 작은 데이터가 위치, pivot의 오른쪽에는 pivot보다 큰 데이터가 위치하게 됨 (= pivot을 기준으로 정렬됨)
# Part 2 : 분할된 리스트에서, 왼쪽 리스트에도 pivot을 설정하여 동일한 방식으로 정렬
# Part 3 : 분할된 리스트에서, 오른쪽 리스트에도 pivot을 설정하여 동일한 방식으로 정렬
# 재귀 함수로 구현 : Part 1 ~ Part 3를 보면 '재귀 함수'와 동작 원리가 같음 ('종료 조건' : 현재 리스트의 원소가 1개인 경우)
# 시간 복잡도 : 평균 시간 복잡도(= O(NlogN))
#            최악의 경우 시간 복잡도(= O(N^2))
#            최선의 경우, pivot값의 위치가 변경되어 분할이 일어날 때마다 정확히 왼쪽 리스트와 오른쪽 리스트를 절반씩 분할할 때
#            -> 데이터가 무작위로 입력되는 경우, 빠르게 동작할 확률이 높음
#            -> But, 호어 분할 방식에 따라 리스트의 가장 왼쪽 데이터를 pivot으로 삼을 때, '이미 데이터가 정렬되어 있는 경우'에는 매우 느리게 동작함
# (cf) 삽입 정렬은 '이미 데이터가 정렬되어 있는 경우' 매우 빠르게 동작하지만, 퀵 정렬은 그와 반대인 것

##### 널리 사용되고 있는 가장 직관적인 형태의 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end): 
    if start >= end:   # 원소가 1개인 경우 종료
        return
    pivot = start      # 피벗은 첫 번째 원소로 정함 (호어 분할(Hoare Partition) 방식)
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:   # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:              # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

##### 파이썬의 장점을 살려 짧게 작성한 퀵 정렬
# 전통 퀵 정렬의 분할 방식과는 조금 다른데, pivot과 데이터를 비교하는 '비교 연산 횟수'가 증가하므로 시간 면에서는 조금 '비효율적'이지만, 더 '직관적이고 기억하기 쉬움'
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]       # 피벗은 첫 번째 원소로 정함 (호어 분할(Hoare Partition) 방식)
    tail = array[1:]       # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot]    # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]    # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))