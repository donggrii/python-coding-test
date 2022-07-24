# 연습문제 - 제일 작은 수 제거하기

# 내 풀이
def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]


# Test Case 1.
# arr = [4, 3, 2, 1]
# return : [4, 3, 2]

# Test Case 2.
# arr = [10]
# return : [-1]
