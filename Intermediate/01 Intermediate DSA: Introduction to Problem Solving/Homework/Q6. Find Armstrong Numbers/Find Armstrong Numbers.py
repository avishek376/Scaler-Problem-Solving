class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        l = []
        for num in range(1,A+1):
            sum = 0

            temp = num
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            if num == sum:
                l.append(num)
        return l
