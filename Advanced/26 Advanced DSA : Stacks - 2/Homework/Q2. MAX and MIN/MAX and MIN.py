class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def rightGreater(A):
            rGreater = [len(A) for i in range(len(A) - 1, -1, -1)]
            stck = []
            for i in range(len(A)):
                while len(stck) > 0 and A[stck[-1]] <= A[i]:
                    rGreater[stck.pop()] = i
                stck.append(i)
            return rGreater

        def leftGreater(A):
            lGreater = [-1 for i in range(len(A))]
            stck = []
            for i in range(len(A) - 1, -1, -1):
                while len(stck) > 0 and A[stck[-1]] < A[i]:
                    lGreater[stck.pop()] = i
                stck.append(i)
            return lGreater

        def leftSmaller(A):
            lSmaller = [-1 for i in range(len(A))]
            stck = []
            for i in range(len(A) - 1, -1, -1):
                while len(stck) > 0 and A[stck[-1]] > A[i]:
                    lSmaller[stck.pop()] = i
                stck.append(i)
            return lSmaller

        def rightSmaller(A):
            rSmaller = [len(A) for i in range(len(A) - 1, -1, -1)]
            stck = []
            for i in range(len(A)):
                while len(stck) > 0 and A[stck[-1]] >= A[i]:
                    rSmaller[stck.pop()] = i
                stck.append(i)
            return rSmaller

        mod = 10 ** 9 + 7
        ans = 0
        LGreater = leftGreater(A)
        RGreater = rightGreater(A)
        LSmaller = leftSmaller(A)
        RSmaller = rightSmaller(A)

        for i in range(len(A)):
            max = A[i] * (i - LGreater[i]) * (RGreater[i] - i)
            min = A[i] * (RSmaller[i] - i) * (i - LSmaller[i])
            val = max - min
            ans += val
        return ans % mod
