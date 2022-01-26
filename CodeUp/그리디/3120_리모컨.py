# https://codeup.kr/problem.php?id=3120

# 아이디어 : 매번 10, 5, 1 중 어떤 값으로 온도를 조절할 지 결정해야 함 -> 범위 구간 나누기
# (ex) 1 ~ 10의 값이 있다면,
# 10을 빼주는 경우 : target이 10보다 클 때 + target이 10 9 8 일 때 (target >= 8)
# 5를 빼주는 경우 : target이 7 6 5 4 3 일 때 (3 <= target <= 7)
# 1을 빼주는 경우 : target이 1 2 일 때 (1 <= target <= 2)
a, b = map(int, input().split())
target = abs(a - b)
cnt = 0

while True:
    if target == 0:
        break
    elif target >= 8:
        target = abs(target - 10)
        cnt += 1
    elif target >= 3 and target <= 7:
        target = abs(target - 5)
        cnt += 1
    else:
        target = abs(target - 1)
        cnt += 1

print(cnt)

# Test Case 1.
# 입력 : 7 34
# 출력 : 5 (7 - 17 - 27 - 32 - 33 - 34)

# Test Case 2.
# 입력 : 22 3
# 출력 : 3 (22 - 12 - 2 - 3)