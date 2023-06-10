class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        setItem = set()

        for item in A:
            start = 2

            while start*start <= item:
                while item % start == 0:
                    item //= start
                    setItem.add(start)
                start += 1
            if item > 1:
                setItem.add(item)
        return len(setItem)
