# 완전탐색 - 최소직사각형

# 내 풀이
# 1. w, h 둘 중 큰 수를 한쪽에 몰아놓기
# 2. (0번째 값들 중 최댓값) x (1번째 값들 중 최댓값)
def solution(sizes):
    sizes = [[max(x, y), min(x, y)] for x, y in sizes]
    result = list(zip(*sizes))
    return max(result[0]) * max(result[1])


# 다른 풀이 1
# w, h 큰 값 중 가장 큰 값 x 작은 값 중 가장 큰 값
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# 다른 풀이 2 : heapq로 최대 힙 구현
import heapq


def solution(sizes):
    mq_w, mq_h = [], []
    for size in sizes:
        w, h = size[0], size[1]
        if w < h:
            w, h = h, w
        heapq.heappush(mq_w, -w)
        heapq.heappush(mq_h, -h)
    return mq_w[0] * mq_h[0]


# 다른 풀이 3
def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    return max([x[0] for x in sizes]) * max([x[1] for x in sizes])


# 다른 풀이 4
# sum(sizes, []) : sizes의 모든 요소가 담긴 1차원 리스트로 변환
# (ex) sum([[60, 50], [30, 70], [60, 30], [80, 40]], []) : [60, 50, 30, 70, 60, 30, 80, 40]
def solution(sizes):
    return max(sum(sizes, [])) * max(min(x) for x in sizes)


# Test Case 1.
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# result : 4000

# Test Case 2.
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
# result : 120

# Test Case 3.
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
# result : 133
