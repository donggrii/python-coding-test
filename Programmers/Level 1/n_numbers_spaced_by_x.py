# 연습문제 - x만큼 간격이 있는 n개의 숫자

# 내 풀이
def solution(x, n):
    return [x * (i + 1) for i in range(n)]


# Test Case 1.
# x, n = 2, 5
# answer : [2, 4, 6, 8, 10]

# Test Case 2.
# x, n = 4, 3
# answer : [4, 8, 12]

# Test Case 3.
# x, n = -4, 2
# answer : [-4, -8]
