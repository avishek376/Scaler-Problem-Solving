# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        while A != None:
            if B < A.val and C < A.val:
                A = A.left
            elif B > A.val and C > A.val:
                A = A.right
            else:
                return A.val
