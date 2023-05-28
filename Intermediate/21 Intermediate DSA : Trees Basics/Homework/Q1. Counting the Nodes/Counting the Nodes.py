# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        self.count = 0
        maxVal = -float('inf')

        def countNodes(root, maxVal):

            if not root:
                return 0
            if root.val > maxVal:
                self.count += 1
            maxVal = max(root.val, maxVal)
            countNodes(root.left, maxVal)
            countNodes(root.right, maxVal)

        countNodes(A, maxVal)

        return self.count