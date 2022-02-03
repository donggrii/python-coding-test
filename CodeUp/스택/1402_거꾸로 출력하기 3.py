# https://codeup.kr/problem.php?id=1402

n = int(input())
data = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    print(data[i])
    
# Test Case.
# < 입력 >
# 5
# 1 3 5 6 8

# < 출력 >
# 8 6 5 3 1