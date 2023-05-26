# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return an integer
    def solve(self, A, B):
        currA = A
        currB = B
        while currA.next != None or currB.next != None:
            if currA.val != currB.val:
                return 0
            currA = currA.next
            currB = currB.next
        return 1
