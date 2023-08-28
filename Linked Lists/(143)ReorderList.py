# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorder(list):
            answer, end = [], len(list)-1

            for i in range(len(list)):
                if i > end:
                    return answer
                elif i == end:
                    answer.append(list[i])
                    return answer
                else:
                    answer.append(list[i])
                    answer.append(list[end])
                end -= 1

        list = []
        
        while head != None:
            list.append(head.val)
            head = head.next
        
        for num in reorder(list)[::-1]:
            head = ListNode(num, head)
