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
        ans = -1

        def height(node):
            nonlocal ans
            if not node:
                return -1
            lht = height(node.left)
            rht = height(node.right)

            ans = max(ans, (lht + rht + 2))
            return max(lht, rht) + 1

        height(A)
        return ans
