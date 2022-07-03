# 연습문제 - 문자열을 정수로 바꾸기

# 내 풀이
def solution(s):
    return int(s[1:]) if s[0] == '+' else -int(s[1:]) if s[0] == '-' else int(s)

# 다른 풀이 1
# 정수형으로 바꿀 때 문자 +, - 는 알아서 양, 음의 기호로 인식하므로
def solution(s):
    return int(s)

# 다른 풀이 2 : 십진수 변환 접근법
# 만약 문제에서 s가 0으로 시작할 수 있고, 중간에 숫자가 아닌 다른 문자열이 포함될 수 있다는 등의 제한조건이 붙는다면 이렇게 푸는 방식이 더 좋을 것
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