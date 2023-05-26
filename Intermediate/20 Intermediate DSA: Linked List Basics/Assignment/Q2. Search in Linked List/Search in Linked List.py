# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        curr = A

        while curr.next != None:
            if curr.val == B:
                return 1
            curr = curr.next
        if curr.val == B:
            return 1
        return 0
