# 문제 : 손님이 요청한 떡의 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이(H)의 최댓값 구하기
#       절단기에 높이(H)를 지정하면 떡을 한 번에 절단하여 높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않음
#       손님은 H 위의 부분으로 잘린 떡을 가져갈 수 있음
# 조건 : 1 <= N(떡의 개수) <= 1,000,000 / 1 <= M(요청한 떡의 길이) <= 2,000,000,000


##### 내 풀이 : 절단기 높이(h)의 초기값을 설정하고, 이진탐색 bisect_right() 함수를 이용하여 h보다 긴 떡들만 남기고, 손님이 요청한 길이(M)과 h로 잘려지는 값들을 비교하며 h의 최댓값 탐색
# < 아이디어 >
# 절단기 높이(h)의 초기값을 (전체 떡의 길이 중 가장 큰 값 - 손님이 요청한 총 길이(M)) 로 설정하면
# 전체 떡 각각에서 h만큼 뺀 값들의 합이 손님이 요청한 총 길이(M)보다 크거나 같을 수밖에 없으므로
# h의 최대값을 찾기 위해 h를 1씩 늘려가며 확인
# 만약, 전체 떡 각각에서 h만큼 뺀 값들의 합이 손님이 요청한 총 길이(M)보다 작아지는 지점이 오면 h - 1 출력

# < 예시 >
# h = 13(초기값)일 때,
# big_lst = [15, 17, 19] -> sum([2, 4, 6]) = 12

# h = 14일 때,
# big_lst = [15, 17, 19] -> sum([1, 3, 5]) = 9

# h = 15일 때,
# big_lst = [17, 19] -> sum([2, 4]) = 6

import sys
from bisect import bisect_right

n, m = map(int, input().split())
total = list(map(int, sys.stdin.readline().rstrip().split()))
total.sort()

h = total[-1] - m      # h의 초기값 설정 (전체 떡의 길이 중 가장 큰 값 - 손님이 요청한 총 길이)
def solution(array, target):
    while True:
        index = bisect_right(array, target)        # 전체 떡 중 target(h)보다 큰 값의 index 찾기
        big_lst = array[index:]                    # target(h)보다 큰 값만 남긴 list
        sum_ = sum([i - target for i in big_lst])  # big_lst에서 target(h)만큼 다 빼준 걸 sum
        if sum_ == m:
            return target
        elif sum_ < m:
            return target - 1
        else:
            target += 1

print(solution(total, h))


# Test Case.
# < input >
# 4 6            # N, M
# 19 15 10 17    # 떡의 개별 높이

# output : 15