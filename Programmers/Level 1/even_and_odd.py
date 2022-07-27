# 연습문제 - 짝수와 홀수

# 내 풀이
def solution(num):
    return "Odd" if num % 2 else "Even"


# 다른 풀이 : & 연산자로 비트 연산
def solution(num):
    return ["Even", "Odd"][num & 1]


# Test Case 1.
# num = 3
# return : "Odd"

# Test Case 2.
# num = 4
# return : "Even"
