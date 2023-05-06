class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        hs = set()
        elements = []
        while A:
            elements.append(A % 10)
            A = A // 10
        n = len(elements)
        if n > 8 or (len(set(elements)) != len(elements)):return 0
        elif n == 1: return 1
        for i in range(n):
            temp = int(elements[i])
            if temp == 0 or temp == 1: return 0
            prd = 1
            for j in range(i, n):
                prd *= elements[j]
                if prd in hs:
                    return 0
                else:
                    hs.add(prd)
        return 1
