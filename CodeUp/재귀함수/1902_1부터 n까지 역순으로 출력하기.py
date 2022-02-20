# https://codeup.kr/problem.php?id=1902
# 문제 : 정수 n이 주어질 때, 반복문을 사용하지 않고 정수 n부터 1까지 출력하는 재귀함수 설계하기

n = int(input())

def recursive(num):
    print(num)
    if num > 1:
        recursive(num - 1)
    
recursive(n)

# Test Case.
# 입력 : 10
# < 출력 >
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1