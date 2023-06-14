class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = 0
        n = len(A)
        r = n - 1
        if n == 1 :
            return A[0]
        while l <= r :
            mid = r-(r-l)//2
            if mid == 0 :
                if A[mid] >= A[mid+1] :
                    return A[mid]
                else :
                    l = mid + 1
            elif mid == n - 1 :
                if A[mid] >= A[mid-1] :
                    return A[mid]
                else :
                    r = mid - 1
            else :
                if A[mid] >= A[mid-1] and A[mid] >= A[mid+1] :
                    return A[mid]
                if A[mid-1] > A[mid] :
                    r = mid - 1
                else :
                    l = mid + 1
