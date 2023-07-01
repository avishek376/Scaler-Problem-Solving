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
    def inorderTraversal(self, A):
        lst = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            lst.append(node.val)
            inOrder(node.right)

        inOrder(A)
        return lst


'''
WITHOUT RECURSION

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []
        node = A
        res = []
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res
'''
