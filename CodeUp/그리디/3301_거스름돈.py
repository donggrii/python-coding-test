# https://codeup.kr/problem.php?id=3301

# 아이디어 : 큰 단위의 화폐부터, 화폐의 종류(K)만큼 반복을 수행하여 카운팅(시간복잡도 O(K))
target = int(input())
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = 0

for coin in coins:
    cnt += target // coin
    target %= coin

print(cnt)

# Test Case.
# 입력 : 54520
# 출력 : 8