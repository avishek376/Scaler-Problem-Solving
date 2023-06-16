Description of approach 1:

Note 1: When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
Note 2: The base (N-1) is the maximum possible.
This implies that if there was a better solution possible, it will definitely have height greater than min(a1, aN).

B * H > (N-1) * min(a1, aN)
We know that, B < (N-1)
So, H > min(a1, aN)

This means that we can discard min(a1, aN) from our set and look to solve this problem again from the start.
If a1 < aN, then the problem reduces to solving the same thing for a2, aN.
Else, it reduces to solving the same thing for a1, aN-1

    TC: O(N)
    SC: O(1)