# Brute Force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = -sys.maxsize - 1
        
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product = product * nums[j]
                maximum = max(product, maximum)
                
        return maximum

# Dynamic Programming
# Time: O(n)
# Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        maximum = nums[0]
        
        for i in range(1, len(nums)):
            tempMax = max(nums[i], max(currMax*nums[i], currMin*nums[i]))
            currMin = min(nums[i], min(currMax*nums[i], currMin*nums[i]))
            
            currMax = tempMax

            maximum = max(currMax, maximum)
                
        return maximum