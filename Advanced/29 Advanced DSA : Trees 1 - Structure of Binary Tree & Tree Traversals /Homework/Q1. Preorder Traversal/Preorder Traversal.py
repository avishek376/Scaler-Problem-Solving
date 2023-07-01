# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        lst = []

        def preOrder(node):
            nonlocal lst
            if not node:
                return
            lst.append(node.val)
            preOrder(node.left)

            preOrder(node.right)

        preOrder(A)
        return lst