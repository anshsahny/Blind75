# Time: O(n)
# Space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        
        answer.append(1)
        
        for i in range(1, len(nums)):
            answer.append(nums[i-1] * answer[i-1])
            
        right = 1
        
        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * right
            right = right * nums[i]
            
        return answer