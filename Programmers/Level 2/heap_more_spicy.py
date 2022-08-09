# 힙(Heap) - 더 맵게

# 내 풀이
# 정확성 100%, 효율성 0% -> min(scoville)을 scoville[0]로만 바꿔줬더니 정확성 100%, 효율성 100%
# min(), max()는 전체 데이터를 확인해야 해서 시간복잡도 O(N)
# heapq를 사용하니까 heap[0]를 보면 제일 작은 값임!
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 또는 scoville.sort()
    
    while len(scoville) > 0:
        if scoville[0] == 0 and scoville[1] == 0:
            return -1
        elif (len(scoville) == 2) and (scoville[0] + (scoville[1] * 2) < K): ### 조건 추가
            return -1
        else:
            if scoville[0] >= K:
                break
            else:
                minimum = heapq.heappop(scoville)
                sec_minimum = heapq.heappop(scoville)
                heapq.heappush(scoville, minimum + (sec_minimum * 2))
                answer += 1
        
    return answer

# 다른 풀이
# while문에 핵심적인 scoville[0] < K 조건을 넣고,
# scoville[0] == 0 and scoville[1] == 0과 (len(scoville) == 2) and (scoville[0] + (scoville[1] * 2) < K)을 동시에 충족하는
# 조건이 len(scoville) <= 1임
import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer += 1
    return answer

# Test Case.
# scoville : [1, 2, 3, 9, 10, 12]
# K : 7
# return : 2