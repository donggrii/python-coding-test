# 연습문제 - 소수 찾기

# 내 풀이 : 에라토스테네스의 체 알고리즘
import math


def solution(n):
    result = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if result[i]:
            j = 2
            while i * j <= n:
                result[i * j] = False
                j += 1
    return sum(result[2:])


# 다른 풀이 : 에라토스테네스의 체를 set 자료형을 이용한 차집합으로 구현
# math.sqrt() 대신 n ** 0.5 이용
def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


# Test Case 1.
# n = 10
# result : 4

# Test Case 2.
# n = 5
# result : 3
