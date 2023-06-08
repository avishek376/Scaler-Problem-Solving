class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        N = len(A)

        def createspf(n):
            spf = [i for i in range(n)]

            i = 2
            while i * i < len(spf):
                if spf[i] == i:
                    j = i * i
                    while j < n:
                        if spf[j] == j:
                            spf[j] = i
                        j += i
                i += 1
            return spf

        def primefactors(spf, n):
            total = 1
            while n > 1:
                prime = spf[n]
                count = 0
                while n % prime == 0:
                    count += 1
                    n = n // prime

                total = total * (count + 1)
            return total

        spf = createspf(max(A) + 1)
        res = []
        for k in range(N):
            value = primefactors(spf, A[k])
            res.append(value)

        return res


'''

prime = []
class Solution:
    def sieve(self, mx):
        global prime
        p = 2
        prime = [-1] * (mx + 1) # Stores the smallest prime factor of integers 1 to max(A)
        while p * p <= mx:
            if prime[p] == -1:
                prime[p] = p
                for i in range(p * p, mx + 1, p):
                    if prime[i] == -1:
                        prime[i] = p
            p += 1
    
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        global prime
        self.sieve(max(A))
        # Using prime factorization to get the number of divisors for every integer
        ans = []
        for i in A:
            if i == 1:
                ans.append(1)
                continue
            num, num_of_divisors = i, 1
            while num > 1:
                cnt = 0
                temp = prime[num]
                while num > 1 and num % temp == 0:
                    num //= temp
                    cnt += 1
                num_of_divisors *= (cnt + 1)
            ans.append(num_of_divisors)
        return ans
'''