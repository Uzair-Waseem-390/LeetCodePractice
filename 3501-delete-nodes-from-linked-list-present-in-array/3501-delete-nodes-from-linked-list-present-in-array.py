# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        temp = dummy
        nums_set = set(nums)   # If we use List it make O(N) time complexity
                               # Id we use Set() this makes O(1) time Complexity

        curr = head
        while curr:
            if curr.val not in nums_set:
                temp.next = ListNode(curr.val)
                temp = temp.next
            curr = curr.next
        return dummy.next
        