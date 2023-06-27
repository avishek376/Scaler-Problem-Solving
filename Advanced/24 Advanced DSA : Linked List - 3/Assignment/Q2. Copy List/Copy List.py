# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        # Add new nodes between original
        t = head
        while (t):
            temp = t.next
            x = RandomListNode(t.label)
            t.next = x
            x.next = temp
            t = temp

        # Assign random pointer of new nodes
        t = head
        while (t):
            if t.random:
                t.next.random = t.random.next
            t = t.next.next

        new_head = head.next

        # Separate original LL and new LL
        t = head
        while (t):
            temp = t.next.next
            if temp:
                t.next.next = temp.next
                t.next = temp
            else:
                t.next.next = None
                t.next = None
            t = temp

        return new_head

