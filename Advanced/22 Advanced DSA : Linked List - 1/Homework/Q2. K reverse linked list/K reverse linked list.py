# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if A == None:
            return None

        curr = A
        prev = None
        temp = None
        count = 0
        while curr != None and count < B:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        A.next = self.reverseList(curr, B)
        return prev




'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverse(A):
    if A.next == None:
        return A
    nxt = A.next
    A.next = None
    rvrsed = reverse(nxt)
    nxt.next = A
    return rvrsed


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        reversedFirst = A
        for i in range(1, B):
            reversedFirst = reversedFirst.next
        prev = ListNode(0)
        prev.next = A
        last = prev
        first = ListNode(0)
        while last.next:
            # take B consecutive nodes and reverse them
            for i in range(1, B + 1):
                last = last.next
            first = prev.next
            prev.next = None
            nxt = last.next
            last.next = None
            reverse(first)
            prev.next = last
            first.next = nxt
            prev = last = first
        return reversedFirst'''

