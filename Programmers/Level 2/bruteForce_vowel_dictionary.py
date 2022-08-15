# 내 풀이 (중복순열 라이브러리 이용)
from itertools import product


def solution(word):
    a = ["A", "E", "I", "O", "U"]
    total = []
    for i in range(1, 6):
        c = ["".join(j) for j in product(a, repeat=i)]
        total.extend(c)
    total.sort()
    return total.index(word) + 1


# 다른 풀이 (DFS)
def solution(word):
    num = {"cur": 0}
    a = ["A", "E", "I", "O", "U"]

    def dfs(found):
        if len(found) > 5:
            return
        if found not in num:
            num[found] = num["cur"]
            num["cur"] += 1
        for s in a:
            dfs(found + s)

    dfs("")
    answer = num[word]
    return answer


# Test Case 1.
# word = "AAAAE"
# result : 6

# Test Case 2.
# word = "AAAE"
# result : 10

# Test Case 3.
# word = "I"
# result : 1563

# Test Case 4.
# word = "EIO"
# result : 1189
