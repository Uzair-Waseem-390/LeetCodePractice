# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#     def append(self, data):
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#             return
#         new_node.next = self.head
#         self.head = new_node
#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,c = None,head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p