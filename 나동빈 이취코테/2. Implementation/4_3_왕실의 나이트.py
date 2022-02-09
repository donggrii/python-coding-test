# 문제 : 체스판과 같은 8 x 8 좌표 평면에서 나이트의 현재 위치 좌표가 주어질 때, 좌표 평면을 벗어나지 않으면서 L자 형태로 이동할 수 있는 모든 경우의 수 구하기
#       (cf) L자 형태 : (수평 2칸 이동 + 수직 1칸 이동) or (수평 1칸 이동 + 수직 2칸 이동)
#       (cf) 행 : 1 ~ 8, 열 : a ~ h
# (참고) 조금 더 까다롭게 문제를 출제한다면 입력 문자가 열과 행이 아닌 1a와 같은 행과 열 형태로 들어왔을 때의 "예외 처리"를 요구할 수도 있음

##### 내 풀이
# 아이디어 : 위치 좌표의 row, column의 index를 이용해서 이동할 수 있는 모든 경우의 수 총 8가지를 대입하고 좌표 평면을 벗어나지 않는 경우의 수 구하기
knight = str(input())                              # c2
row = [str(i) for i in range(1,9)]
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x, y = row.index(knight[1]), col.index(knight[0])  # (1, 2)
move = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1)]
result = 0

for m in move:
    dx, dy = m
    nx, ny = x + dx, y + dy
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue
    else:
        result += 1
        
print(result)

##### 답안 예시
# ord() : 문자의 유니코드 값을 반환하는 함수 (ex. ord('a') = 97, ord('가') = 44032)

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)


# Test Case 1.
# input : a1
# output : 2

# Test Case 2.
# input : c2
# output : 6