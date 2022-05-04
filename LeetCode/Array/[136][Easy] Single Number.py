# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
# 조건 : linear runtime complexity, only constant extra space

# 내 풀이 : 계수 정렬 이용
class Solution:
    def singleNumber(self, nums):
        min_value = min(nums)
        arr = [0] * (max(nums) - min_value + 1)
        
        for i in range(len(nums)):
            arr[nums[i] - min_value] += 1  # nums의 value -> 계수 정렬 arr의 index (arr의 value는 등장 횟수)
        
        for j in range(len(arr)):          # index
            if arr[j] == 1:
                return j + min_value       # 다시 value 값으로 변환

# 다른 풀이 1 : set 함수 이용
class Solution:
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

# 다른 풀이 2-1 : XOR 연산 이용
from functools import reduce

class Solution:
    def singleNumber(self, nums):
    	return reduce(lambda x, y: x ^ y, nums)

# 다른 풀이 2-2 : XOR 연산 이용
class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        return xor

# Test Case 1.
# Input: nums = [2,2,1]
# Output: 1

# Test Case 2.
# Input: nums = [4,1,2,1,2]
# Output: 4

# Test Case 3.
# Input: nums = [1]
# Output: 1

# Test Case 4.
# Input: nums = [[-999, -500, -999, 9000, 9000]
# Output: -500

test = Solution()
print(test.singleNumber([2, 2, 1]))  # 1