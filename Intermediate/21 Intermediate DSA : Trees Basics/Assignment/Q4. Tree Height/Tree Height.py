# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        def heightOfTree(root):
            if not root:
                return 0

            lh = heightOfTree(root.left)
            rh = heightOfTree(root.right)

            return max(lh, rh) + 1

        return heightOfTree(A)
