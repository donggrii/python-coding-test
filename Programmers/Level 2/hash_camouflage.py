# 해시 - 위장

# 내 풀이 (성공)
from collections import defaultdict
from functools import reduce


def solution(clothes):
    dic = defaultdict(int)
    for c in clothes:
        dic[c[1]] += 1
    return reduce(lambda x, y: x * (y + 1), dic.values(), 1) - 1


# 내 풀이 (실패) - 테스트케이스 1번은 조합으로 풀 수 없음
from collections import defaultdict
from itertools import combinations
from functools import reduce


def solution(clothes):
    answer = len(clothes)
    dic = defaultdict(int)
    for c in clothes:
        dic[c[1]] += 1
    total = list(dic.values())

    cases = []
    for i in range(2, len(total) + 1):
        cases.extend(list(combinations(total, i)))
    for case in cases:
        answer += reduce(lambda x, y: x * y, case, 1)
    return answer


# 다른 풀이 1
# (1) 수학적 풀이
# 옷의 종류가 1개일 때 : a, 2개일 때 : (a + b) + (ab), 3개일 때 : (a + b + c) + (ab + bc + ca) + (abc)
# -> 다항식에서 n차식 계수들의 합 : (x + a)(x + b)(x + c) = x^3 + (a + b + c)x^2 + (ab + bc + ca)x + (abc)
# -> x = 1 대입, x^3의 계수는 정답에 포함되지 않으므로 1을 빼줌
# => 정답 = (1 + a)(1 + b)(1 + c) - 1

# (2) 경우의 수로 접근
# 각 옷의 종류 a, b, c개가 있을 때, 해당 옷을 입지 않을 경우(= 1)를 더해줌 : (a + 1), (b + 1), (c + 1)
# 모든 경우의 수를 곱한 후 아무것도 입지 않는 경우(= 1)을 빼줌 : (a + 1) x (b + 1) x (c + 1) - 1

# (3) 조합식으로 접근
# hash_table = {종류1: n, 종류2: m, 종류3: k, 종류4: p}일 때, 각 종류 중 1개를 입을 가짓수 + 안 입을 가짓수
# (nC1 + nC0) + (mC1 + mC0) + (kC1 + kC0) + (pC1 + pC0) - 1
from collections import Counter
from functools import reduce


def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


# 다른 풀이 2
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


# Test Case 1.
# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# return : 5

# Test Case 2.
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# return : 3
