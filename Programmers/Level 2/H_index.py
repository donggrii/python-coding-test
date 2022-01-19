# 정렬 - H-index
# 어떤 과학자가 발표한 논문 n편 중, h번(값) 이상 인용된 논문이 h편(개수) 이상이고 나머지 논문이 h번(값) 이하 인용되었다면 h의 최댓값을 구하라

# 내 풀이
# bisect 이진 탐색 사용
# 나머지 논문이 h번 이하 인용이려면 idx의 왼쪽 인덱스의 값이 h 이하이면 되는데 bisect_left()로 구했기 때문에
# 필연적으로 idx 왼쪽 인덱스 값은 h 이하
# + citations에 없는 인용 횟수값도 적용될 수 있음!
from bisect import bisect_left

def solution(citations):
    result = []
    citations.sort()
    for i in range(citations[-1], -1, -1): # 6, 5, 4, ..., 0 (i = 인용횟수 최댓값부터 0까지 내림차순으로 적용)
        h = i                              # 값
        idx = bisect_left(citations, i)    # 개수
        if (len(citations) - idx) >= h:
            result.append(h)
    return result[0]

# 다른 풀이
# enumerate(start = 1) 이용해서 현재 자신보다 큰 수가 몇개인지 판별
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# 다른 풀이 2
# 시간 복잡도를 위해 h-index가 큰 경우부터 검사하고 조건에 만족하면 출력
# 문제에서는 "h번 이상 인용이 몇편인가? -> 그 편수가 h 이상인가?"의 순서지만
# 이 풀이는 "지금 몇 편이 남았는가? -> 모든 인용횟수가 이 값보다 큰가?(가장 작은 값이 이 값보다 큰가?"로 바꿔서 해결한 것
def solution(citations):
    citations = sorted(citations) # [0,1,3,5,6]
    l = len(citations)            # 5
    for i in range(l):
        if citations[i] >= l-i:  # l-i : i 인덱스 값과 같거나 큰 수의 개수
            return l-i
    return 0

# 다른 풀이 3
# 뒤 인덱스부터 적용해서 인용횟수와 개수 비교
def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(1, len(citations) + 1):
        min_num = citations[-i]
        if min_num >= i:
            answer = i
    return answer

# 다른 풀이 4
# filter() = functools.reduce()
# 하지만, 다른 풀이들에 비해 좀 오래 걸림
def counting(l, n):
    return len(list(filter(lambda x: x >= n, l)))

def solution(citations):
    answer = 0
    for i in range(max(citations)):
        if counting(citations, i) >= i:   # counting(citations, i) : citations에서 i보다 큰 값들의 리스트 길이
            answer = i
        else:
            break
    return answer

# Test Case.
# citations : [3, 0, 6, 1, 5]
# return : 3