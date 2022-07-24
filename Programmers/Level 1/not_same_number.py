# 스택/큐 - 같은 숫자는 싫어

# 내 풀이
# 리스트끼리 비교 or 리스트 슬라이싱 후 리스트끼리 비교하는 다른 풀이보다 '값'끼리만 비교하는 코드가 훨씬 효율적
def solution(arr):
    target = -1
    result = []
    for i in arr:
        if i != target:
            result.append(i)
            target = i
    return result


# 다른 풀이 1 : array[-1:]로 마지막 값을 비교
def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


# 다른 풀이 2 : 오른쪽에 인접한 원소 값이랑 비교해서 값이 다르면 리스트에 포함
# (cf) 리스트 슬라이싱은 index 값이 범위를 초과해도 오류 뜨지 않고 []로 반환됨
def solution(arr):
    return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i + 1: i + 2]]


# 다른 풀이 3
def solution(arr):
    result = []
    for c in arr:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result


# Test Case 1.
# arr = [1, 1, 3, 3, 0, 1, 1]
# answer : [1, 3, 0, 1]

# Test Case 2.
# arr = [4, 4, 4, 3, 3]
# answer : [4, 3]
