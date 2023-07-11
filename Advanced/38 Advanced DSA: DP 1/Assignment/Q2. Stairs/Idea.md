**Approach**

1) This is the most basic dynamic programming problem.

2) We know that we can take 1 or 2 step at a time. So, to take n steps,

3) we must have arrived at it immediately from (n-1) or (n-2) step.

4) If we knew the number of ways to reach (n-1) and (n-2) step,

5) our answer would be the summation of their number of ways.


    TC: O(N)
    SC: O(N)