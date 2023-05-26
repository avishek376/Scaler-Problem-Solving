# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def solve(self, A):
        curr = A

        while curr.next != None:
            print(curr.val, end=" ")
            curr = curr.next
            
        print(curr.val, end=" ")
        print()
