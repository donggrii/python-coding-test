# Summer/Winter Coding(~2018) - 예산

# 내 풀이 : budget에서 d의 가장 작은 값을 빼면서 cnt의 최댓값 구하기
def solution(d, budget):
    d.sort()
    for cnt in range(len(d)):
        budget -= d[cnt]
        if budget < 0:
            return cnt
    return cnt + 1


# 다른 풀이 : budget이 전체 d의 합보다 크거나 같을 때까지 pop으로 d의 최댓값 제거
# 만약, d의 길이가 매우 길고 budget이 작은 수일 경우, 계속 전체 리스트를 sum 해주므로 효율성 문제 발생 가능
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


# Test Case 1.
# d = [1, 3, 2, 5, 4]
# budget = 9
# result : 3

# Test Case 2.
# d = [2, 2, 3, 3]
# budget = 10
# result : 4
