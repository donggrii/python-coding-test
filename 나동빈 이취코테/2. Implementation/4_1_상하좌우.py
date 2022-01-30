# 시뮬레이션 유형 : 일련의 명령에 따라 개체를 차례대로 이동시킴
# 문제 : 이동 계획서가 주어졌을 때, 여행가가 최종적으로 도착하는 좌표값 구하기 (N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됨)

##### 내 풀이
# L, R, U, D를 해시(딕셔너리) 자료형으로 만들어 변환 좌표값을 구하고, 좌표를 벗어나는지 확인 후 x, y값으로 업데이트
n = int(input())
plan = input().split()
move = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}
x, y = 1, 1

for p in plan:
    x_, y_ = move[p]
    change_x, change_y = x + x_, y + y_
    if change_x < 1 or change_x > n or change_y < 1 or change_y > n:
        continue
    x, y = change_x, change_y

print('{} {}'.format(x, y))

##### 답안 예시
# 연산 횟수가 이동 횟수에 비례 => 이동 횟수가 N번인 경우 시간 복잡도는 O(N)
# dx, dy, move_types의 index 순서 맞춰주는 방법
n = int(input())    # N을 입력받기
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)


# Test Case.
# < 입력 >
# n : 5
# 이동 계획서 : R R R U D D

# < 출력 >
# 3 4
# 움직이는 좌표 순서 : (1, 2), (1, 3), (1, 4), (1, 4), (2, 4), (3, 4)