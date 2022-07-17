# 연습문제 - 콜라츠 추측

# 내 풀이
def solution(num):
    cnt = 0
    while cnt < 501:
        if num == 1:
            return cnt
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        cnt += 1
    return -1


# Test Case 1.
# n = 6
# result : 8

# Test Case 2.
# n = 16
# result : 4

# Test Case 3.
# n = 626331
# result : -1
