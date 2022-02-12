# https://codeup.kr/problem.php?id=4040 (어려움)
# 참고 : https://jlog1016.tistory.com/36

# 문제 : 현재 펜션의 예약 상태와 고객의 일정이 주어질 때, 방을 옮기는 최소 횟수를 구하라
# 아이디어 : 
# (1) 맨 처음 or 방을 옮겨야할 때(즉, 전날에는 거주할 수 있지만, 다음 날에는 거주할 수 없을 때 -> check_list는 모두 0이 됨) 다음 날 예약 가능한 방은 1로 만들어 check_list 반환하는 "check" 함수
# (2) check_list를 기준으로 전날과 다음 날 방 예약 상태를 비교하여 거주 가능한 곳이 있는지 체크하고 카운트하는 "solution" 함수
# 방의 개수만큼 zeros_list를 만들어 예약 가능한 방 매일 체크
# 첫 날 check_list는 모두 0으로 시작하여 (1)번 함수를 적용해야 하므로 cnt는 -1부터 시작
n, m = map(int, input().split())
rooms = []
for i in range(n):
    rooms.append(input())
rooms.insert(0, 0)           # index와 일수 맞춰주기
start, end = map(int, input().split())

zeros_list = [0] * m         # 방의 개수만큼 0 생성
def check(cur_room):         # 'O', 'X'로 된 문자열에서 'O'(예약 가능)인 방의 index는 1로 변경하여 예약 상태 체크하는 함수
    result = [0] * m
    
    for idx, status in enumerate(cur_room):
        if status == 'O':
            result[idx] = 1
    
    if result == zeros_list:
        return -1
    
    return result

def solution(data):
    check_list = [0] * m
    cnt = -1
    
    for cur_room in data:
        if check_list != zeros_list:
            for index, checked in enumerate(check_list):
                if checked == 1 and cur_room[index] == 'X':
                    check_list[index] = 0
        
        if check_list == zeros_list:
            cnt += 1
            check_list = check(cur_room)
            if check_list == -1:
                return -1
            
    return cnt

rooms = rooms[start:end]
print(solution(rooms))


# Test Case.
# < 입력 >
# 10 7
# XXXXXXX
# XOXXXXO
# XOXXXXO
# XOXXXOX
# OXXOXOX
# XOXOXOX
# OXXOXOX
# OXXXXOX
# XXXXXXX
# XXXXXXX
# 2 9

# 출력 : 1