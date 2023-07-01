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
        ans = []
        q = deque()
        q.append(A)

        while q:

            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                ans.append(curr.val)
                if curr.right != None:
                    q.append(curr.right)
                if curr.left != None:
                    q.append(curr.left)

        ans.reverse()
        return ans





