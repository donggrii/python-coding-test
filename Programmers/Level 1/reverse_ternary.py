# 월간 코드 챌린지 시즌1 - 3진법 뒤집기

# 내 풀이
def solution(n):
    e = 0
    while True:
        if n < 3 ** e:
            break
        e += 1

    triple = [0] * e
    for i in range(e):
        triple[i] = n // 3 ** (e - i - 1)
        n %= 3 ** (e - i - 1)
        if n == 0:
            break

    final = 0
    for a, b in enumerate(triple):
        final += (3 ** a) * b
    return final


# 다른 풀이 1
# 1. n진수 만들기 : 원하는 값이 0이 될 때까지 n으로 나눈 나머지를 모두 구해 역순으로 붙이기 (몫을 다시 n으로 나눔)
# 2. int(str, n) : n진법으로 이루어진 숫자 문자열 str과 n을 int 함수에 넣으면 10진수 값으로 변환됨
def solution(n):
    result = ""
    while n:
        result += str(n % 3)
        n //= 3
    return int(result, 3)


# 다른 풀이 2 : divmod() 이용
# (ex) divmod(45, 3) = (15, 0)
def solution(n):
    answer = []
    while True:
        if n < 3:
            answer.append(n)
            break
        n, r = divmod(n, 3)
        answer.append(r)
    answer.reverse()
    sum_ = 0
    for i in range(len(answer)):
        sum_ += answer[i] * (3 ** i)
    return sum_


# Test Case 1.
# n = 45
# result : 7

# Test Case 2.
# n = 125
# result : 229
