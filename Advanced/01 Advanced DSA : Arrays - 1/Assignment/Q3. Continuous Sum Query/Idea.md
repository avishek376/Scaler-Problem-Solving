Instead of updating each beggar ranging from i to j, we could update index i with +S and index j + 1 with -S, where S is a donation made by some devotee. So if you want to know the number of coins taken by kth beggar, you just need to find the prefix sum of all the values(coins) from 1 to k(Try to prove it by yourself that values between i to j contains +S as you are doing prefix sum).
This technique is known as difference array and is very helpful in problems which involves range updates.

    TC : O(A+n) , where n denotes the size of B
    SC : O(A)

Example:
N = 5, D = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

Initial array: [0, 0, 0, 0, 0]

After first devotee, if we update i = 1 with +10 and j + 1 = 3 with -10, we get [10, 0, -10, 0, 0].
Now note that if you add 10 to 1st index and subtract 10 with 3rd index and do a prefix sum at every array element, you will get +10 at 1st and 2nd.

After second devotee, if we update i = 2 with +20 and j + 1 = 4 with -20, we get [10, 20, -10, -20, 0].

Similarly, after third devotee, if we update i = 2 with +25 and j + 1 = 6 with -25, we get [10, 45, -10, -20, 0].

Now, if we calculate the prefix sum at every index, we get [10, 55, 45, 25, 25].