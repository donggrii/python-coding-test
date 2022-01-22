price = []
for i in range(5):
    price.append(int(input()))
pasta = price[:3]
juice = price[3:]
answer = (min(pasta) + min(juice)) * 1.1
print(round(answer, 1))