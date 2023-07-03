# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        q = deque()
        rhTraversal = []

        q.append(A)

        if not A:
            return rhTraversal

        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                while curr != None:  # until the right traversing ending we are traversing

                    rhTraversal.append(curr.val)
                    if curr.left != None:
                        q.append(curr.left)
                    curr = curr.right

        return rhTraversal

'''

'''