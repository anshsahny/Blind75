# List to hold all viewed values
# Time: O(n)
# Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = []
        
        for i in range(len(nums)):
            if nums[i] in values:
                return True
            values.append(nums[i])
        
        return False
    
# Sorting original array to see which number repeats
# Time: O(nlogn)
# Space: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False