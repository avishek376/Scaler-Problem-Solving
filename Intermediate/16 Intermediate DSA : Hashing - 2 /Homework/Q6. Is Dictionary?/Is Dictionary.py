class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        dict1={}
        for j in range(len(B)):
            dict1[B[j]] = j

        for i in range(len(A)-1):
            word1 = A[i]
            word2 = A[i+1]
            for k in range(min(len(word1),len(word2))):
                if word1[k] != word2[k]:
                    if dict1[word1[k]] > dict1[word2[k]]:
                        return 0
                    break
            else:
                if len(word1) > len(word2):
                    return 0
        return 1
