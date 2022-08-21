# Categorize By Sorted String
# Time: O(N*KlogK)
# Space: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        
        for word in strs:
            answer[tuple(sorted(word))].append(word)
            
        return answer.values()
    
# Categorize By Count
# Time: O(NK)
# Space: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            answer[tuple(count)].append(word)
            
        return answer.values()