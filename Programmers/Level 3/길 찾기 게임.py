# 자료구조 : 2019 KAKAO BLIND RECRUITMENT > 길 찾기 게임

# 내 풀이
from sys import setrecursionlimit

setrecursionlimit(10000)


def solution(nodeinfo):
    nodeinfo = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]  # 각 좌표 리스트 3번째 인자에 노드 번호 추가
    nodeinfo.sort(key=lambda x: x[0])  # 모든 노드의 x값은 다르므로, x값 기준 오름차순 정렬
    result = [[], []]  # [전위 순회 결과, 후위 순회 결과]

    def recursive(lst):
        if lst:
            highest = (0, -1, 0)  # 루트 노드 정보 : (nodeinfo 내에서의 index, y, 노드 번호)
            # 루트 노드 index 찾기
            for idx, (x, y, n) in enumerate(lst):
                if y > highest[1]:
                    highest = (idx, y, n)

            result[0].append(highest[-1])  # 전위 순회 : 좌, 우 재귀함수 실행 전, 루트 노드 탐색
            left, right = lst[: highest[0]], lst[highest[0] + 1 :]
            recursive(left), recursive(right)
            result[1].append(highest[-1])  # 후위 순회 : 좌, 우 재귀함수 실행 후, 루트 노드 탐색

    recursive(nodeinfo)
    return result
