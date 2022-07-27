# 연습문제 - 자릿수 더하기

# 내 풀이
def solution(n):
    return sum(map(int, str(n)))


# 다른 풀이 : 재귀 구조 이용
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n // 10)


# Test Case 1.
# N = 123
# answer : 6

# Test Case 2.
# N = 987
# answer : 24
