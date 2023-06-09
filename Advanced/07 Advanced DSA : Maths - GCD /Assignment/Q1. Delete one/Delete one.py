def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def prefixGCD(A):
    n = len(A)
    pre = [0] * n
    for i in range(n):
        if i == 0:
            pre[i] = A[i]
        else:
            pre[i] = gcd(A[i], pre[i - 1])
    return pre


def suffixGCD(A):
    n = len(A)
    back = [0] * n
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            back[i] = A[i]
        else:
            back[i] = gcd(A[i], back[i + 1])
    return back


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # pre and back stores the prefix and suffix gcd's respectively
        pre = prefixGCD(A)
        back = suffixGCD(A)
        ans = 0
        maxv = float('-inf')
        for i in range(n):
            if i == 0:
                ans = back[i + 1]
            elif i == n - 1:
                ans = pre[i - 1]
            else:
                ans = gcd(pre[i - 1], back[i + 1])
            maxv = max(maxv, ans)
        return maxv


'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def gcd(A,B):
            rem = B%A
            if rem == 0:
                return A
            return gcd(rem,A)
        
        lgcd = [0 for i in range(len(A))]
        rgcd = [0 for i in range(len(A))]
        
        lgcd[0] = A[0]
        rgcd[len(A)-1] = A[len(A)-1]
        
        getLGCD = lgcd[0]
        for i in range(1,len(A)):
            getLGCD = gcd(A[i],getLGCD)
            lgcd[i] = getLGCD
            
        getRGCD = rgcd[len(A)-1]
        for i in range(len(A)-1,-1,-1):
            getRGCD = gcd(A[i],getRGCD) 
            rgcd[i] = getRGCD
            
        ans = 0    
        maxv = float('-inf')   
        for i in range(len(A)):
            if i == 0:
                ans = rgcd[i+1]
            elif i == len(A)-1:
                ans = lgcd[i-1]
            else:
                ans = gcd(rgcd[i+1],lgcd[i-1])
            maxv = max(ans,maxv)
        return maxv
'''