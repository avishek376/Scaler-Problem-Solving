class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def isPrime(num):
            root = int(math.sqrt(num))
            for i in range(2,root+1):
                if num%i==0:
                    return False
            return True

        mod = 1000000007
        count = 1
        for elem in A:
            if elem > 1 and isPrime(elem):
                count = (count%mod * 2)%mod

        return count-1