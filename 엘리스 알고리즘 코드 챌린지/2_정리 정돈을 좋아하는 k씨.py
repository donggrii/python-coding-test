# 1. 내 풀이
# 정수 : 0, 음수 가능

# k씨가 일하면 정렬된 상태가 유지될까? NO
# <정렬된 상태 유지 안될 때 경우> O
# [1 7 6 8 1] 6 4 5
# [1 1 6 7 8] 6 4 5 : 6
# 1 [7 6 8 1 6] 4 5
# 1 [1 6 6 7 8] 4 5 : 6
# 1 7 6 [8 1 6 4 5]
# 1 7 6 [1 4 5 6 8] : 5
# <정렬된 상태 유지될 때 경우> X
# [1 7 6 8 1] 6 4 5
# [1 1 6 7 8] 6 4 5 : 6
# 1 [1 6 7 8 6] 4 5
# 1 [1 6 6 7 8] 4 5 : 6
# 1 1 6 [6 7 8 4 5]
# 1 1 6 [4 5 6 7 8] : 6

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    i, j, k = map(int, input().split())
    arr_range = arr[i - 1 : j]
    arr_range.sort()
    print(arr_range[k - 1])


# 2. 정답 풀이
import sys


input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
seq = [int(data[i + 2]) for i in range(n)]

index = 2 + n
results = []

for _ in range(m):
    i = int(data[index])
    j = int(data[index + 1])
    k = int(data[index + 2])
    part = sorted(seq[i - 1 : j])
    results.append(part[k - 1])
    index += 3

for result in results:
    print(result)


# Test Case.
# <input>
# 8 3
# 1 7 6 8 1 6 4 5
# 1 5 3
# 2 6 2
# 4 8 3

# <output>
# 6
# 6
# 5
