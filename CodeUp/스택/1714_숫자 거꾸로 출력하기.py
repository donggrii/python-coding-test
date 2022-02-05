# https://codeup.kr/problem.php?id=1714

n = str(int(input()))
result = ''

for i in range(len(n)):
    result += n[len(n)-i-1]

print(result)


# Test Case 1.
# 입력 : 2571
# 출력 : 1752

# Test Case 2.
# 입력 : 1200
# 출력 : 0021

# Test Case 3.
# 입력 : 123456
# 출력 : 654321