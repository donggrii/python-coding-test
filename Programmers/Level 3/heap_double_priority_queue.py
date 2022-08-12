# 힙(Heap) - 이중우선순위큐

# 내 풀이
import heapq


def solution(operations):
    h = []
    for op in operations:
        op = op.split()
        if op[0] == "I":
            heapq.heappush(h, int(op[1]))
        else:
            if not h:
                continue
            elif op[1] == "-1":
                heapq.heappop(h)
            elif op[1] == "1":
                h.remove(max(h))
                heapq.heapify(h)
    return [max(h), heapq.heappop(h)] if h else [0, 0]


# Test Case 1.
# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# return : [0, 0]

# Test Case 2.
# operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# return : [333, -45]
