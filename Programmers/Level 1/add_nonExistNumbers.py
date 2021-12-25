# 월간 코드 챌린지 시즌3 - 없는 숫자 더하기

# 내 풀이
def solution(numbers):
    allNum = [i for i in range(10)]
    answer = [i for i in allNum if i not in numbers]
    return sum(answer)

# 다른 풀이
def solution(numbers):
    return 45 - sum(numbers)

# Test Case 1.
# numbers : [1,2,3,4,6,7,8,0]
# result : 14

# Test Case 2.
# numbers : [5,8,4,0,6,7,9]
# result : 6