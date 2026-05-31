# Given an array of integers nums and an integer target,
# return the indices of the two numbers that add up to target.

Example:
  Input:  nums = [2, 7, 11, 15], target = 9
  Output: [0, 1]  (because nums[0] + nums[1] = 2 + 7 = 9)   

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i