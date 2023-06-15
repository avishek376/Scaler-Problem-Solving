class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        if A[0] != A[1]:
            return A[0]
        elif A[n - 1] != A[n - 2]:
            return A[n - 1]

        s = 2
        e = n - 3
        while s <= e:
            mid = e + (s - e) // 2

            if A[mid] != A[mid - 1] and A[mid] != A[mid + 1]:
                return A[mid]
            if A[mid] == A[mid - 1]:
                mid -= 1
            else:
                pass
            if mid % 2 == 0:
                s = mid + 2
            else:
                e = mid - 1

        return False
