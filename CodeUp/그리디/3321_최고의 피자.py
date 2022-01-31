# https://codeup.kr/problem.php?id=3321
# 문제 : 1달러 당 최대 열량이 되는 값 구하기 (소수점 이하는 버리고 정수로 출력, 같은 토핑 2개 이상 x, 토핑 0개 가능)
# 아이디어 : 토핑 칼로리들을 내림차순으로 정렬, 토핑의 개수(0개 ~ n개)만큼 앞에서부터 더한 칼로리 총합을 가격으로 나눠준 것 중 최대값

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []
for i in range(n):
    d.append(int(input()))
d.sort(reverse = True)          # 토핑 가격 내림차순 정렬
result = []

# 토핑이 0개 ~ n개일 때 가져와서 계산
for top_cnt in range(n+1):
    if top_cnt == 0:
        result.append(int(c/a))
    else:
        price = a + top_cnt * b
        cal = c + sum(d[:top_cnt])
        result.append(int(cal/price))

print(max(result))


##### Test Case.
# < 입력 >
# 3     (토핑 종류 수 N)
# 12 2  (A(도우 가격), B(토핑 가격))
# 200   (C(도우 칼로리))
# 50    (D1(토핑 칼로리))
# 300   (D2(토핑 칼로리))
# 100   (D3(토핑 칼로리))

# < 출력 >
# 37

##### 과정 예시
# 토핑 0개일 때
# 가격 : 12 + 0 * 2 = 12
# 칼로리 : 200
# 1달러당 열량 : 200/12 = "16"

# 토핑 1개일 때
# 가격 : 12 + 1 * 2 = 14
# 칼로리 : 500
# 1달러당 열량 : 500/14 = "35"

# 토핑 2개일 때
# 가격 : 12 + 2 * 2 = 16
# 칼로리 : 600
# 1달러당 열량 : 600/16 = "37"

# 토핑 3개일 때
# 가격 : 12 + 3 * 2 = 18
# 칼로리 : 650
# 1달러당 열량 : 650/18 = "36"