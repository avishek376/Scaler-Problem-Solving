based on the observation that removing any element from the given array makes even indices of succeeding elements
as odd and odd indices of the succeeding elements as even.
Follow the steps below to solve the problem:

Initialize two variables, say evenSum and oddSum,
to store the sum of odd-indexed and even-indexed elements of the given array respectively.

Traverse the array using variable i.
Remove every ith element of the array and update the sum of the remaining even-indexed elements
and the odd-indexed elements based on the above observation. Check if the sums are equal or not.
If found to be true, then increment the count.

Finally, print the count obtained. Check out the complete solution for more clarity.

    TC : O(N)
    SC: O(1)