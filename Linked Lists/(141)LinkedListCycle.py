# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''current, visited = head, []

        while current != None:
            if current in visited:
                return True
            visited.append(current)
            current = current.next

        return False'''

        fast, slow = head, head

        while fast != None and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False