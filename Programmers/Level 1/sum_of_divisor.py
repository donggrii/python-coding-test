# 연습문제 - 약수의 합

# 내 풀이 1 : Greedy
def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])


# 내 풀이 2 : 가운데 약수까지만 구하고, 나머지는 구해놓은 약수를 이용해서 얻기
# 훨씬 시간 효율적인 풀이
import math


def solution(n):
    lst = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    for s in lst[:]:
        extra = n // s
        if extra not in lst:
            lst.append(extra)
    return sum(lst)


# 다른 풀이 1 : 사실상 (n / 2)까지만 검사하면 됨
def solution(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])


# 다른 풀이 2 : filter 이용
def solution(n):
    return sum(filter(lambda x: n % x == 0, range(1, n + 1)))


# Test Case 1.
# n = 12
# return : 28

# Test Case 2.
# n = 5
# return : 6
