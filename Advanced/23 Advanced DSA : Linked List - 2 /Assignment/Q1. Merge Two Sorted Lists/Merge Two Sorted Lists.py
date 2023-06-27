# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        h1 = A
        h2 = B
        t = ListNode(None)
        ans = ListNode(None)

        if h1.val < h2.val:
            ans = h1
            t = h1
            h1 = h1.next
        else:
            ans = h2
            t = h2
            h2 = h2.next
        while h1 != None and h2 != None:
            if h1.val < h2.val:
                t.next = h1
                t = t.next
                h1 = h1.next
            else:
                t.next = h2
                t = t.next
                h2 = h2.next
        if h1 != None:
            t.next = h1
        if h2 != None:
            t.next = h2

        return ans



