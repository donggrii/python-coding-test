# https://www.acmicpc.net/problem/1189

# 내 풀이 (백트래킹을 통한 완전탐색)
# 시작 위치도 카운트, 방문 처리
r, c, k = map(int, input().split())
maps = [list(input()) for _ in range(r)]
total = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global total
    if cnt > k:
        return
    if x == 0 and y == (c - 1) and cnt == k:
        total += 1
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != "T":
                maps[nx][ny] = "T"
                dfs(nx, ny, cnt + 1)
                maps[nx][ny] = "."


maps[r - 1][0] = "T"
dfs(r - 1, 0, 1)
print(total)


# Test Case.
# < input >
# 3 4 6
# ....
# .T..
# ....

# output : 4
