# 연습문제 - 덧칠하기


# 내 풀이
# 한번에 칠할 수 있는 최대 길이 : 롤러의 길이 (m)
# threshold(min + m - 1)보다 큰 값부터 슬라이싱하며 section을 업데이트
def solution(n, m, section):
    cnt = 0
    idx = 0
    while section:
        if section[-1] - section[0] + 1 <= m:  # max - min + 1
            return cnt + 1
        cnt += 1
        thres = section[0] + m - 1  # min + m - 1

        for i, sec in enumerate(section):
            if sec > thres:
                idx = i
                break
        section = section[idx:]


# 다른 풀이 1 : prev 변수를 활용해서 section에 대한 1번의 for문으로 간단 명료하게 풀이
def solution_1(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer


# 다른 풀이 2 : threshold를 활용해서 section에 대한 1번의 for문으로 간단 명료하게 풀이
def solution_2(n, m, section):
    cnt = 0
    thres = 0
    for s in section:
        if s > thres:
            cnt += 1
            thres = s + m - 1
    return cnt


# 다른 풀이 3 : queue 활용
from collections import deque


def solution_3(n, m, section):
    q = deque(section)
    cnt = 0
    while q:
        a = q.popleft()
        cnt += 1
        while q and q[0] - a < m:
            q.popleft()

    return cnt


# Test Case 1.
# n, m = 8, 4
# section = [2, 3, 6]

# result : 2

# Test Case 2.
# n, m = 5, 4
# section = [1, 3]

# result : 1

# Test Case 3.
# n, m = 4, 1
# section = [1, 2, 3, 4]

# result : 4
