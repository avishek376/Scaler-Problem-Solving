# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution:
# @param A : head node of linked list
# @return the head node in the linked list
    def solve(self, A):
        # using Floyd's cycle algo
        slow = A
        fast = A
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                slow = A
                while slow != fast :
                    k = fast
                    slow = slow.next
                    fast = fast.next
                k.next = None
        return A