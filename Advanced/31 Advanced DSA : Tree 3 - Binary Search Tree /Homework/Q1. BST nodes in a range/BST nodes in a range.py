# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

sys.setrecursionlimit(10 ** 5)


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        def validNOdesnBST(node):
            count = 0
            if not node:
                return count

            if node.val >= B and node.val <= C:
                count += 1

            l = validNOdesnBST(node.left)

            r = validNOdesnBST(node.right)
            count += l
            count += r
            return count

        return validNOdesnBST(A)

