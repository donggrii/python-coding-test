# https://codeup.kr/problem.php?id=1901
# 문제 : 정수 n이 주어질 때, 반복문을 사용하지 않고 1부터 정수 n까지 출력하는 재귀함수 설계하기
n = int(input())

# 풀이 1
def recursive_1(num):
    if num != 1:
        recursive_1(num - 1)
    print(num)

recursive_1(n)

# 풀이 2
def recursive_2(num, rec):
    if rec < num:
        print(rec)
        return recursive_2(num, rec + 1)
    elif rec == num:
        return rec
        
print(recursive_2(n, 1))

