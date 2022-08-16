# Brute Force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                answer = max(answer, prices[j] - prices[i])
                
        return answer
    
# One-pass
# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        answer = 0
        
        for i in range(1, len(prices)):
            if minimum < prices[i]:
                answer = max(answer, prices[i] - minimum)
            else:
                minimum = prices[i]
                
        return answer