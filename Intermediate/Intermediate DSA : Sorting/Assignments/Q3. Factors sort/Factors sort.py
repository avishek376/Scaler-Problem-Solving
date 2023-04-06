from functools import cmp_to_key
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        def countFact(a,b):
            c1 = 0
            c2 = 0
            k = int(a**(1/2))
            l = int(b**(1/2))
            for i in range(1,k+1):
                if a%i == 0:
                    if a//i == i:
                        c1+=1
                    else:
                        c1+=2
            for j in range(1,l+1):
                if b%j == 0:
                    if b//j == j:
                        c2+=1
                    else:
                        c2+=2
            if c1 > c2:
                return 1
            elif c1 == c2:
                if(a > b):
                    return 1
                else:
                    return -1
            elif c1 < c2:
                return -1
        A.sort(key=cmp_to_key(countFact))
        return A




