# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer, nums = None, []

        for list in lists:
            while list:
                nums.append(list.val)
                list = list.next

        for num in sorted(nums)[::-1]:
            answer = ListNode(num, answer)
        
        return answer