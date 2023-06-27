# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A is None or A.next is None:  # if the list is empty or has only one node, return the list
            return A

        # initialize three pointers: prev, x, and y
        prev = None  # pointer to the node before x
        x = A  # pointer to the first node
        y = A.next  # pointer to the second node

        # loop through the list and swap adjacent nodes
        while x is not None and y is not None:
            x.next = y.next  # connect x to the node after y
            y.next = x  # connect y to x
            if prev is None:  # if x is the first node, update A to point to y
                A = y
            else:
                prev.next = y  # connect prev to changed y
            prev = x  # update prev to changed x

            x = x.next  # move x to the next pair of nodes
            if x is None:  # if x is None, there are no more pairs to swap
                break
            y = x.next  # move y to the next pair of nodes

        # return the head of the modified list
        return A


'''
# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        start = ListNode("dummy")
        start.next = A
        current = start
        while current.next and current.next.next:
            # swap the two adjacent nodes
            current.next = self.swap(current.next, current.next.next)
            current = current.next.next
        return start.next

    def swap(self, node1, node2):
        node1.next = node2.next
        node2.next = node1
        return node2
'''
