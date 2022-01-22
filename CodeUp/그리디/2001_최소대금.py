# https://codeup.kr/problem.php?id=2001

price = []
for i in range(5):
    price.append(int(input()))
pasta = price[:3]
juice = price[3:]
answer = (min(pasta) + min(juice)) * 1.1
print(round(answer, 1))    # 987.8

# 입력

# 800
# 700
# 900
# 198
# 330