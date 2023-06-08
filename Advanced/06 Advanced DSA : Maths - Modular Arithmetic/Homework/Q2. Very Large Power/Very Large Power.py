class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def power(A,B,M):
            ans = 1
            while B>0:
                if B&1 == 1:
                    ans = (ans*A) % M
                A = (A%M * A%M) % M
                B = B >> 1
            return ans % M
        fact = 1
        mod = 10**9+7
        for i in range(2,B+1):
            fact = (fact*i) % (mod-1)
        ans = power(A,fact,mod)
        return ans



'''

def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res
    
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def solve(self, A, B):
        fact = 1
        mod = 1000000007
        # calculating factorial of B
        for i in range(2, B + 1):
            fact = (fact * i) % (mod - 1)   # (mod-1) is used accoring to Fermat Little theorem.
        return power(A, fact, mod)  # calculating power by divide and conquer
'''