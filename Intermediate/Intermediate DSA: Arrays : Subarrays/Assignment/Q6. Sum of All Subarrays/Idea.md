For each element, if we know how many subarrays do they come in, 
we can easily calculate their contribution to the sum as (Number of Subarrays) * (A[i]).

How do we calculate the number of subarrays for each element?
Let us focus on the definition of a subarray. It is obtained by deleting zero or more elements from either end.
So, for each element, let X be the number of elements to their left, and Y be the number of elements to their right.
Number of required subarrays = (X + 1) * (Y + 1)

We can easily know X and Y from the index of the element.
Let the array be 0 - indexed and N be the length of the array, 
X = i, Y = N - i - 1

Refer to the complete solution for implementation details.

    TC: O(N)
    SC: O(1)