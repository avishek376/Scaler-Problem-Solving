# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        res = []

        q = deque()
        q.append(A)
        dir = "l2r"
        while q:
            n = len(q)
            level = []
            for i in range(n):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)

                    if curr.left != None:
                        q.append(curr.left)
                    if curr.right != None:
                        q.append(curr.right)
            if level:

                if dir == "l2r":
                    res.append(level)
                    dir = "r2l"
                else:
                    res.append(level[::-1])
                    dir = "l2r"
        return res

