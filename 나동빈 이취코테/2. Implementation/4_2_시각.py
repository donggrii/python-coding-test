# 문제 : 정수 N이 주어질 때, 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수 구하기
# 완전 탐색(Brute Forcing) 유형 : 가능한 경우의 수를 모두 검사해보는 탐색 방법. (탐색해야 할 전체 경우의 수가 "100만개 이하"일 경우 사용하면 적절함)
# 하루는 86,400초(24 * 60 * 60). 즉, 전체 경우의 수는 86,400개뿐이므로 3중 반복문으로 모든 시각의 경우를 일일이 확인해도 시간 제한 2초 안에 해결 가능

# 내 풀이
# 아이디어 : 매 시각을 문자열로 바꾼 다음 문자열에 '3'이 포함됐는지 검사
n = int(input())
cnt = 0

for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            time = "{}:{}:{}".format(hour, minute, second)
            if "3" in time:
                cnt += 1

print(cnt)

# 답안 예시
h = int(input())    # H를 입력받기
count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)


# Test Case.
# 입력 : 5
# 출력 : 11475