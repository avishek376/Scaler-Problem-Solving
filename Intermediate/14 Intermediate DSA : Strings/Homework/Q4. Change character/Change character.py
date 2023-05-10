class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        n = len(A)
        arr = [0] * 26
        ans = 0
        for i in A:
            arr[ord(i) - 97] += 1
            if arr[ord(i) - 97] == 1:
                ans += 1
        arr.sort()
        for i in range(26):
            if B - arr[i] >= 0 and arr[i] != 0:
                ans -= 1
                B -= arr[i]
        ans = max(ans, 1)
        return ans

    '''def solve(self, A, B):
        d = dict()
        # run a loop to create dictionary of occurances of each character
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        # sort the dictionary on the basis of occurances
        l = sorted(d.items(), key=lambda x: x[1])

        i = B
        if len(l) == 1:
            return len(l)
        while (i > 0):
            if l[0][1] <= i:
                i -= l[0][1]
                l.pop(0)
            else:
                i -= i

        return len(l)'''

