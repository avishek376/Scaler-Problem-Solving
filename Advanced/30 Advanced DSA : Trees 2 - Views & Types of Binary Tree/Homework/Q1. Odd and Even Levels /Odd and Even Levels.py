# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        q = deque()
        q.append(A)
        level = 1
        oddSum = evenSum = 0
        while q:
            n = len(q)
            if level % 2 != 0:
                for i in range(n):
                    curr = q.popleft()
                    oddSum += (curr.val)
                    if curr.left != None:
                        q.append(curr.left)
                    if curr.right != None:
                        q.append(curr.right)
            else:
                for i in range(n):
                    curr = q.popleft()
                    evenSum += (curr.val)
                    if curr.left != None:
                        q.append(curr.left)
                    if curr.right != None:
                        q.append(curr.right)
            level += 1

        return (oddSum) - (evenSum)


