# 연습문제 - 행렬의 덧셈

# 내 풀이 1 : zip 이용
def solution(arr1, arr2):
    return [list(map(sum, zip(*r))) for r in zip(arr1, arr2)]


# 내 풀이 2 : Greedy
def solution(arr1, arr2):
    final = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr1[0])):
            result.append(arr1[i][j] + arr2[i][j])
        final.append(result)
    return final


# 다른 풀이
def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]


# Test Case 1.
# arr1 = [[1, 2], [2, 3]]
# arr2 = [[3, 4], [5, 6]]
# return : [[4, 6], [7, 9]]

# Test Case 2.
# arr1 = [[1], [2]]
# arr2 = [[3], [4]]
# return : [[4], [6]]
