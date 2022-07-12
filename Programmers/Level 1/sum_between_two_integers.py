# 연습문제 - 두 정수 사이의 합

# 내 풀이
def solution(a, b):
    return a if a == b else sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))


# 다른 풀이 1
def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


# 다른 풀이 2
def solution(a, b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a
    return sum(range(a, b + 1))


# Test Case 1.
# a, b = 3, 5
# return : 12

# Test Case 2.
# a, b = 3, 3
# return : 3

# Test Case 3.
# a, b = 5, 3
# return : 12
