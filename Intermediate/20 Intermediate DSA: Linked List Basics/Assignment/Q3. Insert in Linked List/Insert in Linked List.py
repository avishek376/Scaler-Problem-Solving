# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def solve(self, A, B, C):
        curr = A
        lst = ListNode(B)
        if C == 0:
            lst.next = A
            A = lst
        count = 0
        while curr.next != None:
            if count == C - 1:
                lst.next = curr.next
                curr.next = lst

            curr = curr.next
            count += 1
        if count < C:
            lst.next = None
            curr.next = lst

        return A


