# 문제 : 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된 N x M 크기의 얼음 틀에서 한 번에 만들 수 있는 아이스크림 개수 구하기
#       구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주하고 1개의 아이스크림을 만들 수 있다고 가정

##### 내 풀이 (DFS)
# 아이디어 : 전체 얼음 틀을 순회하면서, 서로 붙어 있어서 1개의 아이스크림을 만들 수 있는 부분을 1로 채워넣는 make_ice 함수로 DFS 구현
n, m = map(int, input().split())
graph = []
for i in range(n):
    row = []
    row_ = str(input())
    for j in range(m):
        row.append(row_[j])
    graph.append(row)

def make_ice(x, y):
    global graph
    graph[x][y] = '1'

    # 상하좌우
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    turn_time = 0
    for r in range(4):
        dx_, dy_ = x + dx[r], y + dy[r]
        if dx_ >= 0 and dx_ < n and dy_ >= 0 and dy_ < m and graph[dx_][dy_] == '0':
            graph[dx_][dy_] = '1'
            make_ice(dx_, dy_)
        else:
            turn_time += 1
    
    if turn_time == 4:
        return
            
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            make_ice(i, j)
            cnt += 1

print(cnt)

##### 답안 예시 (DFS)
# 1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있음
# 3. 1 ~ 2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 셈

n, m = map(int, input().split())   # N, M을 공백으로 구분하여 입력받기

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            
print(result)    # 정답 출력


# Test Case 1.
# < input >
# 4 5
# 00110
# 00011
# 11111
# 00000

# output : 3


# Test Case 2.
# < input >
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111 
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

# output : 8