class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        def gcd(a,b):# calculating GCD
            while(b):
                a, b = b, a % b
            return a
        n=len(A)
        if n<3:
            return n
        ans=0
        hashmap={}
        curmax=0
        overlap=0
        for i in range(n):
            curmax=0
            overlap=0
            for j in range(i+1,n):
                if A[i]==A[j] and B[i]==B[j]:
                    overlap+=1
                else:
                    xdiff=A[j]-A[i]
                    ydiff=B[j]-B[i]
                    z=gcd(xdiff,ydiff)
                    xdiff/=z
                    ydiff/=z
                    if (xdiff,ydiff) in hashmap:
                        hashmap[(xdiff,ydiff)]+=1
                    else:
                        hashmap[(xdiff,ydiff)]=1
                    curmax=max(curmax,hashmap[(xdiff,ydiff)])
            ans=max(ans,curmax+overlap+1)
            hashmap.clear()
        return ans

