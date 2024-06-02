# 자료구조 : 2019 KAKAO BLIND RECRUITMENT > 길 찾기 게임


# 내 풀이
# Python의 재귀 깊이 default 값이 1000인데, 테스트 케이스를 통과하기 위해서는 recursion limit을 변경해줘야 함
from sys import setrecursionlimit

setrecursionlimit(10000)


def solution(nodeinfo):
    nodeinfo = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]  # 각 좌표 리스트 3번째 인자에 노드 번호 추가
    nodeinfo.sort(key=lambda x: x[0])  # 모든 노드의 x값은 다르므로, x값 기준 오름차순 정렬
    result = [[], []]  # [전위 순회 결과, 후위 순회 결과]

    def recursive(lst):
        if lst:
            highest = (0, -1, 0)  # 루트 노드 정보 : (nodeinfo 내에서의 index, y, 노드 번호)
            # 루트 노드 index 찾기 (루트, 왼쪽, 오른쪽 3분할 시작)
            for idx, (x, y, n) in enumerate(lst):
                if y > highest[1]:
                    highest = (idx, y, n)

            result[0].append(highest[-1])  # 전위 순회 : 좌, 우 재귀함수 실행 전, 루트 노드 탐색
            left, right = lst[: highest[0]], lst[highest[0] + 1 :]
            recursive(left), recursive(right)
            result[1].append(highest[-1])  # 후위 순회 : 좌, 우 재귀함수 실행 후, 루트 노드 탐색

    recursive(nodeinfo)
    return result


# 다른 풀이 : 이진 트리 클래스로 생성 후, 전위/후위 순회
from sys import setrecursionlimit

setrecursionlimit(10000)


class BinaryTree:
    """
    1. 이진 트리 class 만들기
        1. Node에는 (left, right) 연결 구조
        2. Node의 value : [노드 번호, x 좌표, y 좌표]
        3. left 혹은 right가 비어 있으면 해당 자리에 None (default는 None)
        4. 신규 Node 삽입 시 left 혹은 right에 할당
        5. 할당된 Node에 value 지정
    2. 이진 트리에 nodeinfo에 있는 Node 정보에 따라 할당
        1. y값을 기준으로 내림차순 정렬 (0번째 Node은 루트 노드)
        2. 첫번째 Node는 루트 노드로, BinaryTree에 [노드 번호, x 좌표, y 좌표] 삽입
        3. 두번째 Node부터는 BinaryTree의 Node들과 비교. x좌표가 작으면 left에 할당, 아니면 right에 할당
    """

    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, val):
        if self.root is None:
            self.root = val
        else:
            if self.root[1] > val[1]:
                if self.left is None:
                    self.left = BinaryTree()
                    self.left.insert(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = BinaryTree()
                    self.right.insert(val)
                else:
                    self.right.insert(val)


def preorder(data):
    """
    전위 순회
    1. 비어 있을 경우 빈 리스트 return
    2. 자기 자신을 먼저 방문 후 left, right 순으로 방문
    """
    if data is None:
        return []
    return [data.root[0]] + preorder(data.left) + preorder(data.right)


def postorder(data):
    """
    후위 순회
    1. 비어 있을 경우 빈 리스트 return
    2. left를 먼저 방문, right 방문, 그 후 자기 자신 방문
    """
    if data is None:
        return []
    return postorder(data.left) + postorder(data.right) + [data.root[0]]


def solution(nodeinfo):
    binary_tree = BinaryTree()
    nodes = [[i + 1, v[0], v[1]] for i, v in enumerate(nodeinfo)]  # [노드 번호, x좌표, y좌표]
    nodes = sorted(nodes, key=lambda x: x[2], reverse=True)  # y좌표 기준 내림차순 정렬

    for node in nodes:
        binary_tree.insert(node)  # y좌표가 가장 큰 루트 노드부터 순차적으로 이진 트리 구성

    pre = preorder(binary_tree)
    post = postorder(binary_tree)
    answer = [pre, post]
    return answer
