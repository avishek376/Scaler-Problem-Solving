class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        digitsList = []  # Split A into list  example A = 236 -> [2,3,6]

        while A:
            digitsList.append(A % 10)
            A = A // 10

        digitsList = list(reversed(digitsList))

        n = len(digitsList)
        digitsProductSet = set()  # Declared set to store product of digitslist

        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= digitsList[j]

                if product in digitsProductSet:
                    return 0
                else:
                    digitsProductSet.add(product)
        return 1