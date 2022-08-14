# Brute Force Method
# Time: O(n^2)
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                
        return []
    
# Two-pass Hash Table
# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        
        for i in range(len(nums)):
            indices[nums[i]] = i
            
        for i in range(len(nums)):
            if target - nums[i] in indices and indices[target - nums[i]] != i:
                return [indices[target - nums[i]], i]
                
        return []
    
# One-pass Hash Table
# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):
            if target - nums[i] in indices and indices[target - nums[i]] != i:
                return [indices[target - nums[i]], i]
            indices[nums[i]] = i
                
        return []