# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        ans = []
        q = deque()
        q.append(A)
        while q:
            level = []
            n = len(q)

            for i in range(n):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left != None:
                    q.append(curr.left)

                if curr.right != None:
                    q.append(curr.right)

            if level:
                ans.append(level)
        return ans