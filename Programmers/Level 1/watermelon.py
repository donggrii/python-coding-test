# 연습문제 - 수박수박수박수박수박수?

# 내 풀이
def solution(n):
    string = "수박"
    if (n % 2) == 1:
        return string * (n // 2) + string[0]
    else:
        return string * (n // 2)
    
# 다른 풀이 1
def water_melon(n):
    return ("수박" * n)[:n]

# 다른 풀이 2
def water_melon(n):
    return "수박" * (n // 2) + "수" * (n % 2)

# 다른 풀이 3
def solution(n):
    return "".join(["수박"[i % 2] for i in range(n)])

# Test Case 1.
# n : 3
# return : "수박수"

# Test Case 2.
# n : 4
# return : "수박수박"