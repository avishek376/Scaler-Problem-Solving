# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        ans = []
        def preorder(node):
            if not node: return

            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)


        preorder(A)
        return ans