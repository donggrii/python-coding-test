# 문제 : N x M 크기의 직사각형에 위치한 육지와 바다 지도에서 캐릭터가 방문한 칸의 수를 출력하기 (전형적인 시뮬레이션 유형)
# < 문제에서 주어진 캐릭터 이동 매뉴얼 >
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.


##### 내 풀이
# 문제에서 "맵의 외곽은 항상 바다로 되어 있다"고 했으므로 맵을 벗어나는 경우는 고려하지 않아도 됨!
# 캐릭터가 "방문한 칸"의 수를 세는 것이므로, 방향을 유지한 채 뒤로 가는 경우에는 count하지 않음!
# 방문했던 칸을 표시하는 행렬 & 원본 지도 행렬을 별개로 다루는 것이 더 정확하고 효율적임!
n, m = map(int, input().split(' '))
x, y, direc = map(int, input().split(' '))
map_ = []
for i in range(n):
    map_.append(list(map(int, input().split(' '))))
cnt = 1
directions = [0, 1, 2, 3]    # 북(-1, 0), 동(0, 1), 남(1, 0), 서(0, -1)
nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]
map_[x][y] = 2               # 현재 위치에 가본 곳이라는 의미의 2로 변경

while True:
    cnt_ = cnt
    for _ in range(4):
        direc = directions[direc - 1]
        nx_, ny_ = x + nx[direc], y + ny[direc]
        if nx_ >= 0 and nx_ < n and ny_ >= 0 and ny_ < m and map_[nx_][ny_] == 0:   # 만약 가보지 않은 곳이거나 육지라면
            x, y = nx_, ny_
            map_[x][y] = 2   # 현재 위치에 가본 곳이라는 의미의 2로 변경
            cnt += 1
            break
        
    if cnt == cnt_:
        direc = directions[direc - 2]
        nx_, ny_ = x + nx[direc], y + ny[direc]
        if nx_ < 0 or nx_ >= n or ny_ < 0 or ny_ >= m or map_[nx_][ny_] == 1:       # nx_, ny_가 바다라면 break
            break
        else:
            x, y = nx_, ny_
            direc = directions[direc - 2]

print(cnt)


##### 답안 예시
n, m = map(int, input().split())              # N, M을 공백으로 구분하여 입력받기
d = [[0] * m for _ in range(n)]               # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
x, y, direction = map(int, input().split())   # 현재 캐릭터의 X 좌표, Y 좌표, 방향 입력받기
d[x][y] = 1    # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 : (★) 문제에서 반복적으로 수행되는 건 함수로 처리하는 게 편리함
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()             # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time = 0

print(count)   # 정답 출력
    

# Test Case.
# < input >
# 4 4        # 4 x 4 맵 생성
# 1 1 0      # (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
# 1 1 1 1    # 첫 줄은 모두 바다
# 1 0 0 1    # 둘째 줄은 바다/육지/육지/바다
# 1 1 0 1    # 셋째 줄은 바다/바다/육지/바다
# 1 1 1 1    # 넷째 줄은 모두 바다

# output : 3