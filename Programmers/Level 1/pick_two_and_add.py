# 월간 코드 챌린지 시즌1 - 두 개 뽑아서 더하기

# 내 풀이
from itertools import combinations


def solution(numbers):
    return sorted(set(map(sum, combinations(numbers, 2))))


# Test Case 1.
# numbers = [2, 1, 3, 4, 1]
# result : [2, 3, 4, 5, 6, 7]

# Test Case 2.
# numbers = [5, 0, 2, 7]
# result : [2, 5, 7, 9, 12]
