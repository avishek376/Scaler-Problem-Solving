Assume that Al, …, Ar is the minimum-unsorted-subarray which is to be sorted.
then min(Al, …, Ar) >= max(A0, …, Al-1)
and max(Al, …, Ar) <= min(Ar+1, …, AN-1)
You can use this to observe and solve.
How would you solve it now?
You can use two pointer technique to solve this question.

    TC: O(N)
    SC: O(1)