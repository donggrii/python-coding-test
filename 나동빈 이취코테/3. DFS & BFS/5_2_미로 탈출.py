# 문제 : N x M 크기의 직사각형 미로가 있을 때, 시작점 (1, 1)에서 미로의 출구 (N, M) 위치로 가는 최소 칸의 개수 구하기 (시작, 마지막 칸 포함해서 셀 것)
#       미로에는 괴물이 있는 곳은 0, 괴물이 없는 곳은 1로 표시되어 있음

##### 내 풀이 (BFS)
# 아이디어 : 이동하는 칸의 개수만큼 graph의 값들을 순차적으로 변경하여 목표 지점인 (n, m)에 도달했을 때 값을 출력
from collections import deque

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y, cnt):
    global graph, visited
    
    queue = deque()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for r in range(4):
        dx_, dy_ = x + dx[r], y + dy[r]
        if dx_ >= 0 and dx_ < n and dy_ >= 0 and dy_ < m and graph[dx_][dy_] == 1 and visited[dx_][dy_] == 0:                
            queue.append([dx_, dy_])
    
    cnt += 1
    while queue:
        x_, y_ = queue.popleft()
        graph[x_][y_] = cnt
        visited[x_][y_] = 1
        bfs(x_, y_, cnt)
    
    if graph[n-1][m-1] != 1:
        return graph[n-1][m-1]

print(bfs(0, 0, 1))

##### 답안 예시 (BFS)
# 아이디어 : 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하는 BFS를 이용하여 해결할 수 있음
#          (1, 1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 변경
# (cf) 답안 예시에서 첫 번째 시작 위치는 다시 방문할 수 있도록 되어 값이 3으로 변경될 여지가 있음
#      하지만, 단순히 가장 오른쪽 아래 위치로 이동하는 것을 요구하므로 해당 문제에서는 정상적으로 작동
from collections import deque

n, m = map(int, input().split())    # N, M을 공백으로 구분하여 입력받기

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))     # BFS를 수행한 결과 출력
    
    
# Test Case.
# < input >
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# < final graph >
# [[3, 0, 5, 0, 7, 0],
#  [2, 3, 4, 5, 6, 7],
#  [0, 0, 0, 0, 0, 8],
#  [14, 13, 12, 11, 10, 9],
#  [15, 14, 13, 12, 11, 10]]

# output : 10