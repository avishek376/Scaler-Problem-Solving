class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        freq1 = [0 for i in range(26)]
        freq2 = [0 for i in range(26)]
        for i in range(len(A)):
            freq1[ord(A[i]) - ord('a')] += 1
            freq2[ord(B[i]) - ord('a')] += 1
        for i in range(26):
            if freq1[i] != freq2[i]:
                return 0
        return 1

    '''
        def solve(self, A, B):
            if len(A)!= len(B):
                return 0
            countDict = {}
            for i in range(len(A)):
                if A[i] not in countDict:
                    countDict[A[i]] = 1
                else:
                    countDict[A[i]] +=1
            for j in range(len(B)):
                if B[j] in countDict:
                    countDict[B[j]] -= 1
                
            keys = countDict.keys()
            
            for key in keys:
                if (countDict[key] != 0):
                    return 0
            return 1
    '''