# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        while A != None:
            if A.val == B:
                return 1
            elif B > A.val:
                A = A.right
            else:
                A = A.left
        return 0
