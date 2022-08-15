# Dictionary
# Time: O(n)
# Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWord = {}
        secondWord = {}
        
        for i in range(len(s)):
            if s[i] not in firstWord:
                firstWord[s[i]] = 1
            else:
                firstWord[s[i]] = firstWord[s[i]] + 1
        
        for i in range(len(t)):
            if t[i] not in secondWord:
                secondWord[t[i]] = 1
            else:
                secondWord[t[i]] = secondWord[t[i]] + 1
        
        return firstWord == secondWord
    
# Sorting
# Time: O(nlogn)
# Space: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWord = sorted(s)
        secondWord = sorted(t)
        
        return firstWord == secondWord