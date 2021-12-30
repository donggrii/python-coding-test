# 2018 KAKAO BLIND RECRUITMENT - [1차] 비밀지도

# 내 풀이
# 이진법 구현
def solution(n, arr1, arr2):
    answer_1 = []
    answer_2 = []
    final = []
    rules = [2 ** i for i in range(n-1, -1, -1)]
    ret = ''
    for ans_1 in arr1:
        for i in rules:
            if ans_1 >= i:
                ret += '#'
                ans_1 -= i
            else:
                ret += ' '
        answer_1.append(ret)
        ret = ''
    for ans_2 in arr2:
        for i in rules:
            if ans_2 >= i:
                ret += '#'
                ans_2 -= i
            else:
                ret += ' '
        answer_2.append(ret)
        ret = ''
    for i in range(n):
        for j in range(n):
            if answer_1[i][j] == ' ' and answer_2[i][j] == ' ':
                ret += ' '
            else:
                ret += '#'
        final.append(ret)
        ret = ''
    return final
    
# 다른 풀이 1
# zip() 사용
# bin() 사용, or 연산자 사용해서 하나라도 1일 때 1을 넣고 둘 다 0일 때 0으로 채워주는 신박한 방법
# rjust(), zfill()로 왼쪽에서부터 0을 채워줌
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:])   # bin() : 이진수로 바꾸는 함수 (ex. bin(5) = '0b101')
        a12 = a12.rjust(n, '0')   # rjust(n, 'a') : n자리수로 바꾸고 오른쪽으로 몰아넣고 왼쪽에 'a'를 채워줌
                                  # ljust(n, 'a') : n자리수로 바꾸고 왼쪽으로 몰아넣고 오른쪽에 'a'를 채워줌
                                  # zfill() : 0을 왼쪽에 채워줌
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer

# 다른 풀이 2
# 정규표현식을 사용해서 0을 채워줌
import re

def solution(n, arr1, arr2):
    answer = ["#"] * n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0' * (n - len(answer[i])) + answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer

# Test Case 1.
# n : 5
# arr1 : [9, 20, 28, 18, 11]
# arr2 : [30, 1, 21, 17, 28]
# 출력 : ["#####","# # #", "### #", "# ##", "#####"]

# Test Case 2.
# n : 6
# arr1 : [46, 33, 33 ,22, 31, 50]
# arr2 : [27 ,56, 19, 14, 14, 10]
# 출력 : ["######", "### #", "## ##", " #### ", " #####", "### # "]