We have to find a way to optimize the time complexity of answering our query.
We can do this by creating an auxiliary array pref,
where pref[i] is the sum of all elements from the beginning to the ith element.

We can easily create the pref array using the following equation:
pref[i] = pref[i - 1] + A[i]

Now, we can answer all our queries in O(1).
The answer to each query will be pref[R] - pref[L - 1].


Refer to the complete solution for more details.


    TC: O(N)
    SC: O(N)