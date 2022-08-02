# https://leetcode.com/problems/number-of-islands/

# 내 풀이
from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        v = [[0] * len(grid[0]) for _ in range(len(grid))]
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.dfs(grid, r, c, v):
                    cnt += 1
        return cnt

    def dfs(self, grid: List[List[str]], row: int, col: int, visited: List[List[int]]) -> bool:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return False

        if grid[row][col] == "1" and visited[row][col] == 0:
            visited[row][col] = 1
            self.dfs(grid, row - 1, col, visited)
            self.dfs(grid, row + 1, col, visited)
            self.dfs(grid, row, col - 1, visited)
            self.dfs(grid, row, col + 1, visited)
            return True
        else:
            return False


# 답지 1
# 동서남북 네 방향 각각 DFS 재귀 호출해 탐색을 마치면, 섬의 개수를 카운트하는 형태로 육지의 개수를 파악
# 이 문제는 방문 경로를 저장할 또 다른 행렬을 생성할 필요 X
class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        # 입력값이 비어 있는 경우에 대한 예외 처리
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # 육지(1)인 곳을 발견하면 self.dfs()를 호출
                    self.dfs(grid, i, j)
                    count += 1  # 모든 육지 탐색 후 카운트 1 증가
        return count

    def dfs(self, grid: List[List[str]], i: int, j: int):
        # 더 이상 땅이 아닌 경우 종료 (백트래킹)
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return

        grid[i][j] = "#"  # 이미 방문했던 곳은 1이 아닌 값으로 마킹 (다시 계산하지 않기 위해 = 가지치기)

        # 동서남북 탐색
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


# 답지 2
# (답지 1)에서 dfs() 함수를 호출할 때마다 grid 변수를 넘겨야 하는 부분을 "중첩함수(Nested Function)"로 개선
class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                return

            grid[i][j] = "#"

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1  # 모든 육지 탐색 후 카운트 1 증가
        return count


# Test Case 1.
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Test Case 2.
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
