# Stack
# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == ')' and stack[len(stack) - 1] != '(':
                    return False
                if s[i] == ']' and stack[len(stack) - 1] != '[':
                    return False
                if s[i] == '}' and stack[len(stack) - 1] != '{':
                    return False
                stack.pop()
        
        return not stack