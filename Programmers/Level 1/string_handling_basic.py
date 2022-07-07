# 연습문제 - 문자열 다루기 기본

# 내 풀이
def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False

# 다른 풀이 1
def solution(s):
    return s.isdigit() and len(s) in (4, 6)

# 다른 풀이 2 : 정규표현식 이용
# ^는 문자열의 처음, $는 문자열의 끝을 의미
# \d는 숫자를 의미하고, {4}|{6}은 숫자가 4번 혹은 6번 반복되는 것을 찾는 것
def solution(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))

# 다른 풀이 3 : try ~ except문, int()
def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6

# Test Case 1.
# s = "a234"
# answer : False

# Test Case 2.
# s = "1234"
# answer : True