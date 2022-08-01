# 2019 KAKAO BLIND RECRUITMENT - 실패율

# 내 풀이
# 1. count()는 O(N)의 시간 복잡도 소요
# 2. 값을 나눠줄 땐, 분모가 0이 되는 경우를 고려할 것
from collections import Counter


def solution(N, stages):
    stats = Counter(stages)
    total = len(stages)
    result = []
    for i in range(1, N + 1):
        failure = stats[i] / total if total > 0 else 0
        result.append((i, failure))
        total -= stats[i]
    result = sorted(result, key=lambda x: (x[1], -x[0]), reverse=True)
    return [r[0] for r in result]


# 다른 풀이 1 : dictionary 이용, 분모가 0일 때 & 아닐 때
from collections import Counter


def solution(N, stages):
    stats = Counter(stages)
    denominator = len(stages)
    result = {}
    for stage in range(1, N + 1):
        if denominator != 0:
            result[stage] = stats[stage] / denominator
            denominator -= stats[stage]
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)


# 다른 풀이 2
# 1. Counter 사용 없이 각 stage에 있는 사람 수를 info에 정리
# 2. 전체 사람 수에서 빼는 것과 반대로 각 stage와 그 이후에 있는 사람 수를 count
def solution(N, stages):
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((i + 1, 0))
        else:
            fail.append((i + 1, yet / be))
    return [item[0] for item in sorted(fail, key=lambda x: x[1], reverse=True)]


# Test Case 1.
# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# result : [3, 4, 2, 1, 5]

# Test Case 2.
# N = 4
# stages = [4, 4, 4, 4, 4]
# result : [4, 1, 2, 3]
