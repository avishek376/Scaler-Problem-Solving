# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        while A != None:
            if A.next != None:
                if A.next.val < A.val:
                    return 0
            A = A.next
        return 1

'''class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        curr = A
        if curr.next == None:
            return 1
        while curr.next != None and curr != None:
            if curr.next.val < curr.val:
                return 0
            curr = curr.next
        return 1'''








