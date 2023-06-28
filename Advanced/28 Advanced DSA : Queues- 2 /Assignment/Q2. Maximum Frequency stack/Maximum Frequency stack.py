from collections import defaultdict, Counter


class FreqStack:

    def __init__(self):
        self.stack = []
        self.hmap1 = Counter()
        self.hmap2 = defaultdict(list)
        self.maxcount = 0

    def push(self, val: int) -> None:
        self.hmap1[val] += 1
        self.maxcount = max(self.maxcount, self.hmap1[val])
        self.hmap2[self.hmap1[val]].append(val)

        return -1

    def pop(self) -> int:
        count = self.maxcount
        if self.hmap2[self.maxcount]:
            ele = self.hmap2[self.maxcount].pop()
            self.hmap1[ele] -= 1

        if not self.hmap2[self.maxcount]:
            self.maxcount -= 1

        return ele


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        freqStack = FreqStack()

        N = len(A)
        ans = []
        value = -1

        for i in range(N):
            val = A[i]
            if val[0] == 1:
                value = freqStack.push(val[1])
                ans.append(value)
            else:
                value = freqStack.pop()
                ans.append(value)

        return ans
