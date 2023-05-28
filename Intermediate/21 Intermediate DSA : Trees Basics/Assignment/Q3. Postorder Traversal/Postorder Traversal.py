# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        lst = []

        def postOrder(root):
            if not root:
                return

            postOrder(root.left)
            postOrder(root.right)
            lst.append(root.val)

        postOrder(A)
        return lst
