# 연습문제 - 문자열 내 마음대로 정렬하기

# 내 풀이
# 1. n번째 문자를 기준으로 정렬
# 2. n번째 문자가 동일한 경우만 잘라서 index 값을 이용해 재정렬
def solution(strings, n):
    strings = sorted(strings, key=lambda x: x[n])
    final = strings.copy()
    char = ""
    idx_s = 0

    for idx, strs in enumerate(strings):
        if char != strs[n]:
            final[idx_s:idx] = sorted(strings[idx_s:idx])
            char = strs[n]
            idx_s = idx
    final[idx_s: len(strings)] = sorted(strings[idx_s: len(strings)])
    return final


# 다른 풀이 1 : lambda 기준 적용 우선순위 이용
# lambda x: (기준 1, 기준2)
# (ex) sorted(temp, key=lambda x: (x[0], -x[1])) : 0번째 원소로 오름차순 정렬 후, 1번째 원소로 내림차순 정렬
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


# 다른 풀이 2 : 먼저 1번 정렬하고 그 다음 n번째 문자를 기준으로 정렬
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


# 다른 풀이 3 : operator.itemgetter() 이용
from operator import itemgetter


def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))


# Test Case 1.
# strings = ["sun", "bed", "car"]
# n = 1
# return : ["car", "bed", "sun"]

# Test Case 2.
# strings = ["abce", "abcd", "cdx"]
# n = 2
# return : ["abcd", "abce", "cdx"]
