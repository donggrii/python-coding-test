# https://www.acmicpc.net/problem/1260

# 문제 : 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력
#       (정점 번호는 1번 ~ N번. 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료)

# 내 풀이
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())  # 간선이 연결하는 두개의 정점
    
    # 각 정점들이 연결하고 있는 정점들의 리스트(graph)를 2차원 배열로 생성
    # (ex) Test Case 1 : [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
    graph[a].append(b)
    graph[b].append(a)

# ascending sort : (문제 조건) 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
for i in range(1, n + 1):
    graph[i].sort()

# DFS
def dfs(value):
    visited[value] = True
    print(value, end = ' ')
    
    for i in graph[value]:
        if visited[i] == False:
            dfs(i)

# BFS
def bfs(value):
    queue = deque([value])
    visited[value] = True
    
    while queue:
        num = queue.popleft()
        print(num, end = ' ')
        
        for i in graph[num]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(v)
visited = [False] * (n + 1)   # initialize visited list
print()                       # dfs(v)와 bfs(v)의 출력 줄바꿈
bfs(v)

# Test Case 1.
# < input >
# 4 5 1      # N, M, V : 정점의 개수 N(1 <= N <= 1,000), 간선의 개수 M(1 <= M <= 10,000), 탐색을 시작할 정점의 번호 V
# 1 2        # 아래 M개의 줄에는 간선이 연결하는 두 정점의 번호
# 1 3
# 1 4
# 2 4
# 3 4

# < output >
# 1 2 4 3
# 1 2 3 4

# Test Case 2.
# < input >
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

# < output >
# 3 1 2 5 4
# 3 1 4 2 5

# Test Case 3.
# < input >
# 1000 1 1000
# 999 1000

# < output >
# 1000 999
# 1000 999