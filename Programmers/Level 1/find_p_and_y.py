# 코딩테스트 연습 > 연습문제 > 문자열 내 p와 y의 개수

# 내 풀이
# Counter() 객체에 존재하지 않는 key 값을 호출하면 오류가 나지 않고, 0을 return
from collections import Counter
def solution(s):
    count = Counter(s.lower())
    if 'p' in count or 'y' in count:
        if count['p'] == count['y']:
            return True
        else:
            return False
    else:
        return True

# 다른 풀이 1
# count() 집계 함수 이용
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

# 다른 풀이 2
from collections import Counter
def solution(s):
    c = Counter(s.lower())
    return c['p'] == c['y']


# Test Case 1.
# s = "pPoooyY"
# answer : True

# Test Case 2.
# s = "Pyy"
# answer : False