# 구현 : 연습문제 - 하노이의 탑


# 내 풀이
# N개의 원반이 start에서 to로 via를 거쳐서 이동
# hanoi(N, start, to, via) = hanoi(N-1, start, via, to) + hanoi(1, start, to) + hanoi(N-1, via, to, start)
def solution(n):
    answer = []  # (start, to)

    def hanoi(n, start, to, via):
        if n == 1:
            answer.append([start, to])
        else:
            hanoi(n - 1, start, via, to)
            answer.append([start, to])
            hanoi(n - 1, via, to, start)

    hanoi(n, 1, 3, 2)

    return answer
