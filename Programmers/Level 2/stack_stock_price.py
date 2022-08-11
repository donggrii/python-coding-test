# 스택/큐 - 주식가격

# 내 풀이
def solution(prices):
    result = []
    last = len(prices) - 1
    for idx in range(len(prices)):
        if idx == last:
            result.append(0)
            break
        if prices[idx] > prices[idx + 1]:
            result.append(1)
        else:
            for i in range(idx + 1, len(prices)):
                if i == last and prices[idx] <= prices[i]:
                    result.append(last - idx)
                if prices[idx] > prices[i]:
                    result.append(i - idx)
                    break
    return result


# 다른 풀이 1 : stack 이용, 가장 빠름
# 1. 주식 가격이 떨어지지 않는다면 stack에 차례대로 [index, price]를 담기
# 2. 현재 위치 prices[i]가 이전 값(stack[-1][1])보다 작으면, 즉 주식 가격이 떨어진 경우,
#    -> prices[i]를 기준으로 이전 stack에 담겨 있던 주식 가격들과 비교하면서 pop으로 꺼내 answer에 바로 업데이트
#    -> stack에는 현재 주식 가격보다 같거나 큰 값들만 담겨있는 상태 유지됨
# 3. 마지막까지 stack에 남아 있는 값들은 끝까지 주식 가격이 떨어지지 않았으므로 일괄적으로 계산하여 answer에 업데이트
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer


# 다른 풀이 2 : Queue 이용, 두번째로 빠름
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)
    return answer


# 다른 풀이 3 : 깔끔하지만 가장 느린 코드
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


# Test Case 1.
# prices = [1, 2, 3, 2, 3]
# return : [4, 3, 1, 1, 0]

# Test Case 2.
# prices = [1, 2, 3, 2, 3, 1]
# return : [5, 4, 1, 2, 1, 0]

# Test Case 3.
# prices = [3, 1]
# return : [1, 0]
