# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        ans = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(A)
        return ans