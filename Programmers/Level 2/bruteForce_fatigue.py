# 완전탐색 - 피로도

# 내 풀이 : 순열을 이용한 완전 탐색
from itertools import permutations


def solution(k, dungeons):
    count = []
    for case in permutations(range(len(dungeons))):
        cnt, energy = 0, k
        for d in case:
            if energy < dungeons[d][0]:
                break
            else:
                energy -= dungeons[d][1]
                cnt += 1
        count.append(cnt)
    return max(count)


# 다른 풀이 1
from itertools import permutations


def solution(k, dungeons):
    visited = 0
    for p in permutations(dungeons):
        have, count = k, 0
        for need, cost in p:
            if have >= need:
                have -= cost
                count += 1
        visited = max(visited, count)
    return visited


# 다른 풀이 2 : DFS 풀이
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer


# Test Case.
# k = 80
# dungeons = [[80, 20], [50, 40], [30, 10]]
# result : 3
