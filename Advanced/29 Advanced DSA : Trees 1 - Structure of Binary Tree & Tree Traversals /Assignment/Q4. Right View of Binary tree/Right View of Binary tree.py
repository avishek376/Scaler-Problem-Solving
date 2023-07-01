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
        res = []
        q = deque()
        q.append(A)
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if curr:
                    if i == n-1:
                        res.append(curr.val)

                    if curr.left != None:
                        q.append(curr.left)
                    if curr.right != None:
                        q.append(curr.right)

        return res


