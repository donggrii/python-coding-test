# 연습문제 - 평균 구하기

# 내 풀이
def solution(arr):
    return sum(arr) / len(arr)


# 다른 풀이
from functools import reduce


def solution(arr):
    return reduce(lambda x, y: x + y, arr) / len(arr)


# Test Case 1.
# arr = [1, 2, 3, 4]
# return : 2.5

# Test Case 2.
# arr = [5, 5]
# return : 5
