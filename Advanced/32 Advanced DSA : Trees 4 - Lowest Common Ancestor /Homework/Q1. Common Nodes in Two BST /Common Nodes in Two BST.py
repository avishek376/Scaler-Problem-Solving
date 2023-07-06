# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):
        firstHMap = {}
        summ = 0
        mod = 10 ** 9 + 7

        def firstInOrder(node):
            nonlocal firstHMap
            if not node:
                return

            if node.val in firstHMap:
                firstHMap[node.val] += 1
            else:
                firstHMap[node.val] = 1

            firstInOrder(node.left)
            firstInOrder(node.right)

        def secondTreeTraversal(root):
            nonlocal summ
            if not root:
                return
            if root.val in firstHMap:
                summ += root.val

            secondTreeTraversal(root.left)
            secondTreeTraversal(root.right)

        firstInOrder(A)
        secondTreeTraversal(B)
        return summ % mod
