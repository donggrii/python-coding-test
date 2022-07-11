# 연습문제 - 이상한 문자 만들기
# 각 단어별 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾸기

# 내 풀이
def solution(s):
    words = s.split(' ')
    for i, word in enumerate(words):
        word = list(word)
        for idx, char in enumerate(word):
            word[idx] = char.lower() if idx % 2 else char.upper()
        words[i] = ''.join(word)
    return ' '.join(words)


# 다른 풀이 1 : map 이용
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


# 다른 풀이 2 : 그리디
def solution(s):
    idx = 0
    result = ''

    for i in s:
        if i != ' ':
            if idx % 2 == 0:
                result += i.upper()
                idx += 1
            else:
                result += i.lower()
                idx += 1
        else:
            result += i
            idx = 0

    return result


# Test Case.
# s = "try hello world"
# return : "TrY HeLlO WoRlD"
