# 연습문제 - 문자열을 정수로 바꾸기

# 내 풀이
def solution(s):
    return int(s[1:]) if s[0] == '+' else -int(s[1:]) if s[0] == '-' else int(s)

# 다른 풀이 1
# 정수형으로 바꿀 때 문자 +, - 는 알아서 양, 음의 기호로 인식하므로
def solution(s):
    return int(s)

# 다른 풀이 2
# 현재 문제에서는 s가 0으로 시작하지 않는다는 조건이 있어 int(str)으로 쉽게 풀 수 있었지만,
# 만약 문제에서 s가 0으로 시작할 수 '있다'는 제한조건이 붙었다면 이렇게 푸는 방식이 더 좋을 것
def solution(s):
    result = 0
    
    for idx, number in enumerate(s[::-1]):  # -1234 -> 4321-
        if number == '-':
            result *= -1
        elif number == '+':
            result *= 1
        else:
            result += int(number) * (10 ** idx)

    return result

# Test Case 1.
# input : "1234"
# output : 1234

# Test Case 2.
# input : "-1234"
# output : -1234