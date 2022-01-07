# 연습문제 - JadenCase 문자열 만들기

# 내 풀이
# 공백이 2자리 이상일 경우도 고려해야 함 (ex) "3people   unFollowed me" -> "3people   Unfollowed Me"
# s.split()    : (x)
# s.split(" ") : (o)
def solution(s):
    lst = s.split(" ")            # 공백 기준으로 나누기
    
    # 첫 글자 대문자로(만약 첫 글자가 숫자면 넘어가기), 나머지 소문자로
    for i in range(len(lst)):     # lst = ["3people", "", "", "Unfollowed", "Me"]
        if len(lst[i]) > 0:       # 공백이 아닌 경우만
            if lst[i][0].isdigit():
                lst[i] = lst[i][0] + lst[i][1:].lower()
            else:
                lst[i] = lst[i][0].upper() + lst[i][1:].lower()
    return ' '.join(lst)

# 다른 풀이
# capitalize() 함수 : 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환
# (cf) title() 함수 : 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환(But, 첫번째 글자가 숫자일 경우 그 다음 문자가 대문자로 됨) -> 이 문제에서는 답이 아님
#               (ex) "3people unFollowed me for the last week" -> "3People Unfollowed Me For The Last Week"
def solution(s):
    return " ".join([word.capitalize() for word in s.split(" ")])

# Test Case 1.
# s : "3people unFollowed me"
# return : "3people Unfollowed Me"

# Test Case 2.
# s : "for the last week"
# return : "For The Last Week"