class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        k = B % n

        def myReverse(arr, s, e):
            while s < e:
                arr[s], arr[e] = arr[e], arr[s]
                s += 1
                e -= 1

        s, e = 0, n - 1
        myReverse(A, s, e)
        s, e = 0, k - 1
        myReverse(A, s, e)
        s, e = k, n - 1
        myReverse(A, s, e)

        return A

