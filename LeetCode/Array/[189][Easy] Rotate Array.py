# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
# 조건 : 
# 1. Do not return anything, modify nums in-place instead.
# 2. Do it in-place with O(1) extra space.

##### 내 풀이
# 내 풀이 1 : pop & insert
class Solution:
    def rotate(self, nums, k):
        for _ in range(k):
            a = nums.pop()
            nums.insert(0, a)
        # print(nums)
        
# 내 풀이 2 : Use Auxiliary Space
class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        nums_copy = nums.copy()
        for i in range(len(nums)):
            nums[i] = nums_copy[i - k]
        # print(nums)
        
# 내 풀이 3 : Reverse Array & Reverse elements divided at k index
class Solution:
    def rotate(self, nums, k):
        nums.reverse()
        k %= len(nums)
        one = k // 2
        two = (len(nums) - k) // 2
        for i in range(one):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for j in range(two):
            nums[-(j+1)], nums[k+j] = nums[k+j], nums[-(j+1)]
        # print(nums)
        
# 내 풀이 4 : Brute Force (Not Correct: RunTimeError)
class Solution:
    def rotate(self, nums, k):
        for _ in range(k):
            for i in range(len(nums) - 1):
                nums[i], nums[-1] = nums[-1], nums[i]
        # print(nums)

##### 다른 풀이
# 다른 풀이 1 : Use Auxiliary Space (Naive Way)
#             -> By adding another auxiliary to store moved nums, and finally replace nums[:] = auxiliary
# Time Complexity : O(n) -> Let n be num's length
# Space Complexity : O(n) -> Store Auxiliary
class Solution:
    def rotate(self, nums, k):
        auxArr = [0] * len(nums)
        k %= len(nums)
        for i in range(len(nums)):
            auxArr[(i + k) % len(nums)] = nums[i]
        nums[:] = auxArr

# 다른 풀이 2 : Reverse Array (Correct Way!!)
#             * Explanation :
#             Say we have nums = [1, 2, 3, 4, 5, 6, 7], k = 3
#             Step 1: Reverse nums => [7, 6, 5, 4, 3, 2, 1]
#             Step 2: Reverse from 0 ~ k and k+1 ~ len(nums) => nums = [5, 6, 7, 1, 2, 3, 4]
# Time Complexity : O(n) -> Let n be num's length, takes twice to loop through whole array => O(2n) = O(n)
# Space Complexity : O(1)
class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverseArray(0, len(nums) - 1, nums)
        self.reverseArray(0, k - 1, nums)
        self.reverseArray(k, len(nums) - 1, nums)
    
    def reverseArray(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

# 다른 풀이 3 : Cyclic Move Elements
# Time Complexity : O(n) -> Let n be num's length
# Space Complexity : O(1)
class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        start, move = 0, 0
        while move < len(nums):
            current, prev = start, nums[start]
            while True:
                nextIdx = (current + k) % len(nums)
                nums[nextIdx], prev = prev, nums[nextIdx]
                current = nextIdx
                move += 1
                if current == start:
                    break
            start += 1


# Test Case 1.
# input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# output: [5, 6, 7, 1, 2, 3, 4]

# Test Case 2.
# input: nums = [-1, -100, 3, 99], k = 2
# output: [3, 99, -1, -100]

Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)  # [5, 6, 7, 1, 2, 3, 4]
Solution().rotate([-1, -100, 3, 99], 2)      # [3, 99, -1, -100]