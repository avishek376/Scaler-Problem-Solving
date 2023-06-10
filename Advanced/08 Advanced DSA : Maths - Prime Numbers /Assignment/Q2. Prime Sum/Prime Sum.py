class Solution:
    def sieve(self, N):
        # Generate isPrime List less equal than N
        isPrime = [1] * (N + 1)
        isPrime[0] = 0
        isPrime[1] = 0
        # Sieve of Erastothenes
        for i in range(2, N + 1):
            if (isPrime[i] == 0):
                continue
            if (i > N // i):
                break
            for j in range(i * i, N + 1, i):
                isPrime[j] = 0
        return isPrime

    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        isPrime = self.sieve(A);

        ans = []
        for i in range(2, A + 1):
            if (isPrime[i] == 1 and isPrime[A - i] == 1):
                ans = [i, A - i]
                return ans
        return ans


'''class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        def checkPrime(N):
            x = 2
            while x * x <= N:
                if N % x == 0:
                    return False
                x += 1
            return True

        for x in range(2, A):

            if checkPrime(x) and checkPrime(A - x):
                return [x, A - x]'''
