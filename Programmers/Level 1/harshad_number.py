# 연습문제 - 하샤드 수
# 양의 정수 x가 하샤드 수 : x의 자릿수의 합으로 x가 나누어져야 함

# 내 풀이
def solution(x):
    return x % sum([int(x) for x in str(x)]) == 0


# 다른 풀이
def solution(x):
    return x % sum(map(int, str(x))) == 0


# Test Case 1.
# arr : 10
# return : True

# Test Case 2.
# arr : 12
# return : True

# Test Case 3.
# arr : 11
# return : False

# Test Case 4.
# arr : 13
# return : False
