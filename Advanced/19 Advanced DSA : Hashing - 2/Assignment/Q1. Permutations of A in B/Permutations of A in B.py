def same(hash1, hash2):
    for i in range(0, 26):
        if hash1[i] != hash2[i]:
            return 0  # not a permutation of A
    return 1  # got a permutation of A in B

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        hash1 = [0] * 26
        hash2 = [0] * 26
        count = 0
        # count frequency of each char in A
        for i in range(0, n):
            hash1[ord(A[i]) - ord("a")] += 1
        # count frequency of each char in first window of size n in B
        for i in range(0, n):
            hash2[ord(B[i]) - ord("a")] += 1
        count += same(hash1, hash2)
        # move current window 1 step ahead
        j = 0
        for i in range(n, m,):
            hash2[ord(B[j]) - ord("a")] -= 1
            hash2[ord(B[i]) - ord("a")] += 1
            count += same(hash1, hash2)
            j += 1
        return count

'''class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        def checkPermutaion(dict1, dict2):
            for char in dict1:
                if dict3.get(char):
                    if dict1[char] != dict2[char]:
                        return False
                else:
                    return False
            return True

        n = len(A)
        m = len(B)

        s, e = 0, n - 1
        count = 0
        mod = 10 ** 9 + 7

        if n > m:
            return 0

        dict1 = {}
        dict3 = {}

        # freq of A
        for i in range(n):
            if A[i] not in dict1:
                dict1[A[i]] = 1
            else:
                dict1[A[i]] += 1

        # freq of B upto n
        for i in range(s, n):
            if B[i] not in dict3:
                dict3[B[i]] = 1
            else:
                dict3[B[i]] += 1
        if checkPermutaion(dict1, dict3):
            count += 1
        s += 1
        e += 1
        # sliding window
        while e < m:
            if B[e] in dict3:
                dict3[B[e]] += 1
            else:
                dict3[B[e]] = 1
            dict3[B[s - 1]] -= 1

            if checkPermutaion(dict1, dict3):
                count += 1
            s += 1
            e += 1
        return count'''
