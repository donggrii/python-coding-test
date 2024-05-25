# 탐색, 자료구조 : 완전탐색 - 전력망을 둘로 나누기


# 내 풀이
# 1. 전선 1개를 끊었을 때, 무조건 전력망이 둘로 나눠진다고 가정하고 풀기
# 2. 1번이 안되면, 전선 1개를 끊은 후 v1, v2 각각에 연결된 송전탑 개수를 더해서 전체 송전탑의 개수(n)가 되는지 확인하기
def solution(n, wires):
    def count_top(start, check):
        # start 지점과 연결된 송전탑의 개수 세는 함수
        for idx, x in enumerate(matrix[start]):
            if x == 1 and check[idx] == 0:
                check[idx] = 1
                check = count_top(idx, check)
        return check

    matrix = [(n + 1) * [0] for i in range(n)]
    matrix.insert(0, 0)
    for v1, v2 in wires:  # 연결된 트리 구조의 전력망
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1

    min_diff = float("inf")
    for v1, v2 in wires:
        check = [0] * (n + 1)  # 연결된 송전탑의 개수를 확인하기 위한 체크 변수
        # 전선 1개씩 끊기
        matrix[v1][v2] = 0
        matrix[v2][v1] = 0

        # 연결된 송전탑 개수 세기 (v1 지점에서 시작)
        # 전선 1개를 끊었을 때, v1과 연결된 송전탑은 1 아니면 0
        check[v1] = 1
        check = count_top(v1, check)

        nums = sum(check)
        # 전력망이 둘로 나눠졌으므로 나머지 송전탑 개수는 전체에서 빼서 구하기
        other_nums = n - nums
        diff = abs(nums - other_nums)
        # 두개로 나뉘어진 송전탑 개수의 차이가 가장 적은 값으로 업데이트
        min_diff = min(min_diff, diff)

        # 끊었던 전선 다시 돌려놓기
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1
    return min_diff


# [다른 사람 풀이에서 배울 점]

# for sub in (wires[i + 1 :] + wires[:i] for i in range(len(wires))):
# => (ex) wires = [[1,2],[2,3],[3,4]]일 때, ([1:] + [:0]), ([2:] + [:1]), ([3:] + [:2])
# => 즉, wires 리스트 안의 한 개의 원소(i)를 제외한 모든 경우의 수를 각각 구할 수 있음
