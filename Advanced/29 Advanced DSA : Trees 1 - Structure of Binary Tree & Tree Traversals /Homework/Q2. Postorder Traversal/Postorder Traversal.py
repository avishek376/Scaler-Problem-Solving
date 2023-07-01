# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import sys
sys.setrecursionlimit(10**5)
class Solution:
	# @param A : root node of tree
	# @return a list of integers

    def postorderTraversal(self, A):
        lst = []
        def postOrder(node):
            nonlocal lst
            if not node:
                return
            postOrder(node.left)
            postOrder(node.right)
            lst.append(node.val)

        postOrder(A)
        return lst