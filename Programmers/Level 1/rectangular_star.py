# 연습문제 - 직사각형 별찍기

# 내 풀이
a, b = map(int, input().strip().split(" "))
for _ in range(b):
    for _ in range(a):
        print("*", end="")
    print()


# 다른 풀이 1
a, b = map(int, input().strip().split(" "))
print(("*" * a + "\n") * b)


# 다른 풀이 2
a, b = map(int, input().strip().split(" "))
for _ in range(b):
    print("*" * a)


# Test Case.
# input : 5 3

# < output >
# *****
# *****
# *****
