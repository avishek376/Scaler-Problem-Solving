# Function to return the sum of the count
# of set bits in the integers from 1 to n
mod = 1000000007


def countSetBits(n):
    global mod

    # Ignore 0 as all the bits are unset
    n += 1;

    # To store the powers of 2
    powerOf2 = 2;

    # To store the result, it is initialized
    # with n/2 because the count of set
    # least significant bits in the integers
    # from 1 to n is n/2
    cnt = n // 2;

    # Loop for every bit required to represent n
    while (powerOf2 <= n):

        # Total count of pairs of 0s and 1s
        totalPairs = n // powerOf2;

        # totalPairs/2 gives the complete
        # count of the pairs of 1s
        # Multiplying it with the current power
        # of 2 will give the count of
        # 1s in the current bit
        cnt += (totalPairs // 2) * powerOf2;
        cnt %= mod

        # If the count of pairs was odd then
        # add the remaining 1s which could
        # not be groupped together
        if (totalPairs & 1):
            cnt += (n % powerOf2)
        else:
            cnt += 0
        cnt %= mod;
        # Next power of 2
        powerOf2 <<= 1;

        # Return the result
    return cnt;


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return countSetBits(A)





'''
        class Solution:
            # @param A : integer
            # @return an integer
            def solve(self, A):
                mod = 1000000007

                def largestPowerOf2inRange(A):
                    x = 0
                    while (1<<x) <= A:
                        x += 1
                    return x-1

                if A <= 1:
                    return A
                x = largestPowerOf2inRange(A)
                bitsUpTo2RaiseX = x*(1<<(x-1))
                msbXToA = A - (1<<x) + 1
                rest = A - (1<<x)
                ans = bitsUpTo2RaiseX + msbXToA + self.solve(rest)
                return ans%mod

'''