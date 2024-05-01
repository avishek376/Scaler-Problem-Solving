class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0
        n = len(height)
        res = 0
        l, r = 0, n - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


'''
Approach 1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)

        ans = 0

        prefixMax = [0] * len(A)
        suffixMax = [0] * len(A)

        prefixMax[0] = A[0]
        suffixMax[n - 1] = A[n - 1]

        for i in range(1, n):
            prefixMax[i] = max(A[i], prefixMax[i - 1])

        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(A[i], suffixMax[i + 1])

        for i in range(1, n - 1):
            blockade = min(prefixMax[i - 1], suffixMax[i + 1])
            amount = blockade - A[i]
            if amount > 0:
                ans += amount
        return ans
        
        
        TC: O(N) | SC: O(N)
        
'''
