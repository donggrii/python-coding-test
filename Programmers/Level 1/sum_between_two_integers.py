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


# 다른 풀이 3 : 수학 공식 (n x (n + 1) / 2) 변형 이용
# 시간 복잡도 : O(1)
# n -> (abs(a - b) + 1) : a ~ b 사이의 정수 개수
# (n + 1) / 2 -> (a + b) / 2 : 처음과 끝 2개 정수씩 쌍을 이뤘을 때 모두 합이 같다는 걸 이용해서 다 더하고 2로 나누기
def solution(a, b):
    return (abs(a - b) + 1) * (a + b) / 2


# Test Case 1.
# a, b = 3, 5
# return : 12

# Test Case 2.
# a, b = 3, 3
# return : 3

# Test Case 3.
# a, b = 5, 3
# return : 12
