# 연습문제 - 정수 내림차순으로 배치하기

# 내 풀이
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))


# Test Case.
# n = 118372
# return : 873211
