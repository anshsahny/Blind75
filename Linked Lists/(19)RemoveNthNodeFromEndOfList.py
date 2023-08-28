# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            curr, next, prev = head, None, None

            while curr != None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            return prev

        def remove(head):
            count, current = 1, head

            while current.next != None:
                if n == 1:
                    return head.next
                else:
                    if count == n-1:
                        current.next = current.next.next
                        return head
                    count += 1
                    current = current.next
        
        if head.next == None:
            return None
        
        return reverse(remove(reverse(head)))
