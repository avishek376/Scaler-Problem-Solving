# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if not A:
            return

        # invert left and right subtrees separetly
        self.invertTree(A.left)
        self.invertTree(A.right)

        # swap the trees and return root
        A.left, A.right = A.right, A.left
        return A