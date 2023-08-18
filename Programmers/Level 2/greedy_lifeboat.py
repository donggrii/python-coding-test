# 탐욕법(Greedy) - 구명보트

# 내 풀이
# < 풀이 아이디어 >
# 1. 내림차순으로 정렬
# 2. 맨 앞의 사람과 맨 뒤의 사람을 같이 보낼 수 없으면 맨 앞의 사람만 태워 보냄
# 3. (핵심) 맨 앞의 사람의 무게가 limit의 절반 이하가 되면 남은 사람 수 // 2 출력 (홀짝인지 확인 필요)
from collections import deque


def solution(people, limit):
    cnt = 0
    people.sort(reverse=True)  # 내림차순 정렬
    queue = deque(people)
    while len(queue) > 0:
        if queue[0] > (limit / 2):  # 맨 앞의 사람 몸무게가 limit의 절반 이하인지 확인
            if len(queue) > 1:
                if queue[0] + queue[-1] <= limit:  # 맨 앞 사람과 맨 뒤의 사람을 같이 보낼 수 있을 때
                    cnt += 1
                    queue.popleft()
                    queue.pop()
                else:  # 맨 앞 사람과 맨 뒤의 사람을 같이 보낼 수 없으면 맨 앞 사람만 태워 보내기
                    cnt += 1
                    queue.popleft()
            else:  # 섬에 1명의 사람만 남을 때(len(queue) == 1)
                cnt += 1
                queue.pop()
        else:
            cnt += len(queue) // 2 if len(queue) % 2 == 0 else len(queue) // 2 + 1
            break

    return cnt


# 다른 풀이
# 투 포인터 활용
# 아이디어 : 짝 지었을 때만 2명씩 나가므로, 전체 인원에서 짝지은 수만 빼주면 보트의 수가 나옴 (천재인듯..)
def solution(people, limit):
    answer = 0
    people.sort()  # 오름차순 정렬

    a = 0  # a, b의 2개 index를 따로 설정해주는 좋은 아이디어
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer  # 여기가 핵심!


# 다른 풀이 2
# deque의 popleft(), pop(), appendleft() 함수 사용
from collections import deque


def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))  # 오름차순 정렬

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:  # deque_people에 1명의 사람만 있었을 때
            return result + 1
        right = deque_people.pop()
        if left + right > limit:  # left + right <= limit인 경우는 popleft, pop으로 left와 right가 빠지고, result += 1이 됨
            deque_people.appendleft(left)  # 몸무게가 제일 작은 사람만 다시 추가해주므로, 몸무게가 제일 높은 right의 index는 하나씩 낮아짐
        result += 1  # right에 해당하는 사람만 태워 보냄
    return result


# 다른 풀이 3
# list에서 pop()을 사용하므로 현재는 효율성 테스트에서 실패하지만, deque를 사용하여 같은 논리로 풀면 해결됨
def solution(people, limit):
    answer = 0
    poo = sorted(people)
    while poo:
        if len(poo) == 1:
            answer += 1
            break
        if poo[0] + poo[-1] > limit:
            poo.pop()
            answer += 1
        else:
            poo.pop(0)
            poo.pop()
            answer += 1
    return answer


# Test Case 1.
# people : [70, 50, 80, 50]
# limit : 100
# return : 3
# 내림차순 정렬 : [80, 70, 50, 50]

# Test Case 2.
# people : [70, 80, 50]
# limit : 100
# return : 3
# 내림차순 정렬 : [80, 70, 50]

# Hidden Test Case 1.
# people : [40, 50, 150, 160]
# limit : 200
# return : 2
# 내림차순 정렬 : [160, 150, 50, 40]

# Hidden Test Case 2.
# people : [100, 500, 500, 900, 950]
# limit : 1000
# return : 3
# 내림차순 정렬 : [950, 900, 500, 500, 100]
