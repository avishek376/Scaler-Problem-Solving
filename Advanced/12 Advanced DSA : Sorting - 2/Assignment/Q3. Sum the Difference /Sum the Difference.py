class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		mod = 10**9+7
        n = len(A)
        ## will use the contribution technique
        ## contri = > sum+=A[i]*(pow(2,i) - pow(2,n-1-i) )
        A = sorted(A)
        def calc_pow(x):
            return 1<<x
        ans = 0
        for i in range(n):
            ans+= A[i] * (calc_pow(i) - calc_pow(n-i-1))
        return ans%mod