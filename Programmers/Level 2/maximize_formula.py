# 2020 카카오 인턴십 - 수식 최대화

# 내 풀이
# 아이디어 : 우선순위대로 괄호 씌우기
# 1. *, +, - 마다 순열(permutations)로 모든 경우의 수 구하기
# 2. 순서대로 split하고 괄호에 담아서 우선적으로 계산하도록 하고 (이 때, f 문자열 포매팅 이용)
# 3. 최종적으로 문자열로 다시 합쳐서 eval로 계산, abs 씌우기
from itertools import permutations

def solution(expression):
    spec = ['*', '+', '-']
    answer = []

    for per in permutations(spec):      # 총 6가지 경우의 수
        first, second = per[0], per[1]  # '*', '+'
        lst = []
        for ex in expression.split(first):              # '*'로 split : ["100-200", "300-500+20"]
            ex_ = [f"({i})" for i in ex.split(second)]  # '+'로 split하고 괄호 씌우기 : ["(300-500)", "(20)"]
            lst.append(f"({second.join(ex_)})")         # lst = ["(100-200)", "(300-500)+(20)"]
        fin = first.join(lst)
        answer.append(abs(eval(fin)))                   # answer = ["((100-200))*((300-500)+(20))"]
    return max(answer)     # 이렇게 구한 상금 다 리스트에 담아서 그 중 최댓값 리턴

# 다른 풀이
# re.split('regex', string_variable) : regex를 기준으로 split해줌
# _ex = ex[:]로 복사해서 기호가 나타나는 곳의 index를 이용하여 양 옆 값을 계산하여 index-1으로 변경
# _ex에서 index, index+1에 해당하는 값 삭제
import re
from itertools import permutations

def solution(expression):
    # 1
    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split('(\D)', expression)

    # 2
    a = []
    for x in op:     # 모든 경우의 수
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    # 3
    return max(abs(int(x)) for x in a)

# Test Case 1.
# expression : "100-200*300-500+20"
# result : 60420

# Test Case 2.
# expression : "50*6-3*2"
# result : 300