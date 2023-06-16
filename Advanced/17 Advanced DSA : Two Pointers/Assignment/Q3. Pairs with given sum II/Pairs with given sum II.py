class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        s, e = 0, n - 1

        ans = 0
        mod = 10 ** 9 + 7

        while s < e:
            currentSum = A[s] + A[e]
            if currentSum > B:
                e -= 1
            elif currentSum < B:
                s += 1

            else:
                # Since array is sorted and if we  came to a point where A[p1] == A[p2]
                # then all the remaining elements are equal only
                # So we are breaking after calculating no of pairs
                # Ex [1 2 2 2 2 4 5] all 2 are equal
                # Note: - ((repeat) * (repeat - 1) / 2) 4C2 pairs combination
                if A[s] == A[e]:
                    x = e - s + 1
                    ans += ((x * (x - 1)) // 2) % mod
                    break
                # if they are not equal we just find out how many times p1 and p2
                # elements are repeating and add all pairs formed by them
                else:
                    a = 1
                    b = 1
                    while A[s] == A[s + 1]:
                        a += 1
                        s += 1
                    s += 1

                    while A[e] == A[e - 1]:
                        b += 1
                        e -= 1
                    e -= 1
                    ans += (a * b) % mod
        return ans % mod
