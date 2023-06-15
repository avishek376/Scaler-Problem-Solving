class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        l = 1
        r = n
        ans = 0

        # Sliding Window
        def maxSubSum(arr, k, B):
            n = len(arr)
            s = 0
            e = k
            sum1 = sum2 = 0
            result = 0
            for i in range(s, e):
                sum1 += arr[i]
                if sum1 > B:
                    return False

            s += 1
            result = sum1
            sum2 = sum1
            while e < n:
                sum2 = sum2 - arr[s - 1] + arr[e]
                result = max(result, sum2)

                s += 1
                e += 1
            if result > B:
                return False
            return True

        while l <= r:
            mid = r + (l - r) // 2

            if maxSubSum(A, mid, B):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
