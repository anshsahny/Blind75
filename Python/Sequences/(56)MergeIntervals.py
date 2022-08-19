# Sorting
# Time: O(nlogn) -> Sort is O(nlogn)
# Space: O(logn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        
        intervals.sort()
        
        for item in intervals:
            if not answer or answer[-1][1] < item[0]:
                answer.append(item)
            else:
                answer[-1][1] = max(answer[-1][1], item[1])
            
        return answer
        