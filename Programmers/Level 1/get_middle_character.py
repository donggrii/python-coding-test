# 연습문제 - 가운데 글자 가져오기

# 내 풀이
def solution(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1 : len(s) // 2 + 1]


# 다른 풀이
def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]


# Test Case 1.
# s = "abcde"
# return : "c"

# Test Case 2.
# s = "qwer"
# return : "we"
