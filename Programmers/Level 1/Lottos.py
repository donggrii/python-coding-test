# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) - 로또의 최고 순위와 최저 순위

# 내 풀이
def solution(lottos, win_nums):

    min_cnt = 0
    zero_cnt = 0

    for i in lottos:
        if i == 0:
            zero_cnt += 1      # 0 개수
        for j in win_nums:
            if i == j:
                min_cnt += 1   # 일치 개수
                continue

    maxNum = min_cnt + zero_cnt
    minNum = min_cnt
    numList = [maxNum, minNum]
    answer = []
    rank = 0

    for i in numList:
        if i == 6:
            rank = 1
        elif i == 5:
            rank = 2
        elif i == 4:
            rank = 3
        elif i == 3:
            rank = 4
        elif i == 2:
            rank = 5
        else:
            rank = 6
        answer.append(rank)

    return answer

# 다른 풀이 1
# count()와 배열 순서를 활용한 ranking
def solution_1(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)  # 0 개수
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1         # 일치 개수
    return rank[cnt_0 + ans], rank[ans]

# 다른 풀이 2
# 같은 숫자가 2개 이상 담겨있지 않으므로 일치 개수 세는 방법에 set 활용 : len(set(lottos) & set(win_nums))
def solution_2(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

# 다른 풀이 3
# Pythonic code using List Comprehension
def solution_3(lottos, win_nums):
    zero = lottos.count(0)                    # 0 개수
    a = [x for x in lottos if x in win_nums]  # 일치 개수
    max = zero + len(a)
    min = len(a)

    max = 7 - max if max >= 1 else 6
    min = 7 - min if min >= 1 else 6
    return [max, min]

# Test Case 1.
# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
# result : [3, 5]

# Test Case 2.
# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]
# result : [1, 6]

# Test Case 3.
# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]
# result : [1, 1]