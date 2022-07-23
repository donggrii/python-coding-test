# 해시 - 폰켓몬

# 내 풀이
def solution(nums):
    return len(set(nums)) if len(set(nums)) <= len(nums) // 2 else len(nums) // 2


# 다른 풀이
def solution(nums):
    return min(len(nums) // 2, len(set(nums)))


# Test Case 1.
# nums = [3, 1, 2, 3]
# result : 2

# Test Case 2.
# nums = [3, 3, 3, 2, 2, 4]
# result : 3

# Test Case 3.
# nums = [3, 3, 3, 2, 2, 2]
# result : 2
