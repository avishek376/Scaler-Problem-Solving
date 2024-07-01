class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def countCows(arr,mid):
            cowCounter=1
            loc=A[0]
            for i in range(1,len(arr)):
                if arr[i]-loc>=mid:
                    cowCounter += 1
                    loc=arr[i]
            return cowCounter
        ans = 0
        A.sort()
        n = len(A)
        mini= 10**8
        for i in range(n-1):
            mini = min((A[i+1]-A[i]),mini)
        l = mini
        h = A[n-1]-A[0]
        while l <= h:
            mid = l+(h-l)//2
            if countCows(A,mid)>=B:
                ans = mid
                l= mid+1
            else:
                h = mid-1
        return ans
