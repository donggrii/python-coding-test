# 연습문제 - 정수 제곱근 판별

# 내 풀이
def solution(n):
    x = n ** 0.5
    return (x + 1) ** 2 if int(x) == x else -1


# 다른 풀이 1 : '% 1' 연산으로 실수, 정수 판별
def solution(n):
    x = n ** 0.5
    return -1 if x % 1 else (x + 1) ** 2


# 다른 풀이 2 : float type에서 사용할 수 있는 is_integer()
def solution(n):
    x = n ** 0.5
    return -1 if not x.is_integer() else (x + 1) ** 2


# 다른 풀이 3 : pow 함수
def solution(n):
    x = pow(n, 0.5)
    return pow(x + 1, 2) if int(x) == x else -1


# Test Case 1.
# n = 121
# return : 144

# Test Case 2.
# n = 3
# return : -1
