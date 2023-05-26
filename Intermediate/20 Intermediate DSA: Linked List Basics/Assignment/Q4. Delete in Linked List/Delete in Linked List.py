# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        curr = A
        count = 0
        if B == 0:
            A = A.next
        while count < B-1:
                curr = curr.next
                count += 1

        temp = curr.next
        curr.next = temp.next

        return A
