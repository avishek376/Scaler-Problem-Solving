class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        c = 0 #no of elements less than B
        sp = 0 #no of swaps required
        ans = float('inf')
        n = len(A)
        for i in range(len(A)):
            if A[i] <= B:
                c+=1
        # no of swaps required in first window of size c
        for i in range(c):
            if A[i] > B:
                sp+=1

        ans = min(sp , ans )

        #now sliding our window to get min swaps
        for i in range(c,n):
            if A[i-c] <=B and A[i] > B:
                sp+=1
            elif A[i-c] > B and A[i] <=B:
                sp-=1
            ans = min(ans , sp)

        return ans
