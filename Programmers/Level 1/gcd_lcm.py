# 연습문제 - 최대공약수와 최소공배수

# 내 풀이
def solution(n, m):
    n, m = min(n, m), max(n, m)

    def gcd(n, m):
        return gcd(m % n, n) if m % n else n

    def lcm(n, m):
        return n * m / gcd(n, m)

    return [gcd(n, m), lcm(n, m)]


# 다른 풀이 1
def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return [c, int(a * b / c)]


# 다른 풀이 2 : math.gcd() 이용
from math import gcd


def solution(a, b):
    gcd_ = gcd(a, b)
    lcm_ = (a * b) // gcd_
    return [gcd_, lcm_]


# Test Case 1.
# n, m = 3, 12
# return : [3, 12]

# Test Case 2.
# n, m = 2, 5
# return : [1, 10]
