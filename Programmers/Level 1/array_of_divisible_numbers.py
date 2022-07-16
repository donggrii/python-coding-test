# 연습문제 - 나누어 떨어지는 숫자 배열

# 내 풀이
def solution(arr, divisor):
    result = [n for n in arr if n % divisor == 0]

    return [-1] if len(result) == 0 else sorted(result)


# 다른 풀이
# A or B 연산 : A가 True면 A를 반환하고, A가 False면 B를 반환
def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]


# Test Case 1.
# arr = [5, 9, 7, 10]
# divisor = 5
# return : [5, 10]

# Test Case 2.
# arr = [2, 36, 1, 3]
# divisor = 1
# return : [1, 2, 3, 36]

# Test Case 3.
# arr = [3, 2, 6]
# divisor = 10
# return : [-1]
