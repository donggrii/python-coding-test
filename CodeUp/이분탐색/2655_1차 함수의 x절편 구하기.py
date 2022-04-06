# https://codeup.kr/problem.php?id=2655

a, b = map(int, input().split())
x = -(b / a)

print(f"{x:.4f}")
# 위와 동일
# print("{:.4f}".format(x))
# print(format(x, '.4f'))

# Test Case.
# input : 1 5
# output : -5.0000