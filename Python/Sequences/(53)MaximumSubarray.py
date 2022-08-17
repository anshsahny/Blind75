# Brute Force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -sys.maxsize - 1
        
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total = total + nums[j]
                maximum = max(total, maximum)
        
        return maximum
    
# Dynamic Programming, Kadane's Algorithm
# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        maximum = nums[0]
        
        for i in range(1, len(nums)):
            total = max(nums[i], total + nums[i])
            maximum = max(total, maximum)
        
        return maximum