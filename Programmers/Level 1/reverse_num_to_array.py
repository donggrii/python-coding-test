# 연습문제 - 자연수 뒤집어 배열로 만들기

# 내 풀이
def solution(n):
    result = list(str(n))
    result.reverse()
    return list(map(int, result))


# 다른 풀이 1 : reversed()
def solution(n):
    return list(map(int, reversed(str(n))))


# 다른 풀이 2 : [::-1]
def solution(n):
    return [int(i) for i in str(n)][::-1]


# Test Case.
# n = 12345
# return : [5, 4, 3, 2, 1]
