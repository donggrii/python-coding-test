# 완전탐색 - 카펫

# 내 풀이 : 약수 이용
def solution(brown, yellow):
    row_col = [(yellow // col, col) for col in range(1, int(yellow ** 0.5) + 1) if yellow % col == 0]
    for r, c in row_col:
        if (r + 2) * (c + 2) - yellow == brown:
            return [r + 2, c + 2]


# 다른 풀이 1 : 바깥 둘레 길이 이용 & 케이스를 미리 다 찾아놓을 필요 X
def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0 and 2 * (i + yellow // i) == brown - 4:
            return [(yellow // i) + 2, i + 2]


# 다른 풀이 2 : 길이, 넓이 식으로 2개의 식 만들고 이차방정식 만들어서 근의 공식 적용
# 근의 공식 : ax^2 + bx + c = 0, x = (-b ± math.sqrt(b^2 - 4ac)) / 2a
# (1) b + y = w x h
# (2) b = (2 x w) + (2 x (h - 2))
#     => h = (b + 4) / 2 - w
# (1) + (2) : w^2 - (b + 4)/2 x w + (b + y) = 0
import math


def solution(brown, yellow):
    w = ((brown + 4) / 2 + math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2
    h = ((brown + 4) / 2 - math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2
    return [w, h]


# Test Case 1.
# brown, yellow = 10, 2
# return : [4, 3]

# Test Case 2.
# brown, yellow = 8, 1
# return : [3, 3]

# Test Case 3.
# brown, yellow = 24, 24
# return : [8, 6]
