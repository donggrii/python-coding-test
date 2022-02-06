# https://codeup.kr/problem.php?id=3117

# 아이디어 : 0이 나왔을 때는 직전에 나왔던 숫자 삭제, 마지막 출력값은 리스트 내 모든 숫자의 합
k = int(input())
lst = []

for _ in range(k):
    num = int(input())
    if num != 0:
        lst.append(num)
    else:
        if lst:
            del lst[-1]

print(sum(lst))


# Test Case.
# < 입력 >
# 10
# 1
# 3
# 5
# 4
# 0
# 0
# 7
# 0
# 0
# 6

# 출력 : 7