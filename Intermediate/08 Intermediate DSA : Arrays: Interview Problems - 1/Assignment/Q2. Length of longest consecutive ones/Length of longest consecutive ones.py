class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        ans = 0
        for i in range(n):
            count += int(A[i])
        if count == n:
            return n
        for i in range(n):
            if int(A[i]) == 0:
                l = 0
                r = 0
                for j in range(i - 1, -1, -1):
                    if int(A[j]) == 1:
                        l += 1
                    else:
                        break
                for j in range(i + 1, n):
                    if int(A[j]) == 1:
                        r += 1
                    else:
                        break
                length = l + r + 1
                if length > count:
                    length = count
                if ans < length:
                    ans = length

        return ans
