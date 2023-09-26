import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # A is the array of values
        # B is the array of weights
        # C is the knapsack capacity
        n = len(A)
        # Create a list of tuples (value, weight) for each item
        items = [(A[i], B[i]) for i in range(n)]

        # Sort the items by their value-to-weight ratio in decreasing order
        items.sort(key=lambda x: x[0] / x[1], reverse=True)

        # Initialize the total value of the knapsack
        value = 0

        # Iterate over the items
        for i in range(n):
            # If the weight of the current item can fit in the knapsack, add its full value to the total value
            if items[i][1] <= C:
                C -= items[i][1]
                value += items[i][0]
            # Otherwise, add a fraction of its value based on how much weight can fit in the knapsack
            else:
                value += C * (items[i][0] / items[i][1])
                break

        return int(value * 100)
