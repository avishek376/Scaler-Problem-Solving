We can find the value of M by looping from 1 to min(A, B) and storing the maximum M, which satisfies the equation A%M == B%M.

But this approach will take time complexity of O(min(A, B)). So that will not work.

We will try to find the pattern by fixing the value of A and taking different B values.

    Suppose A = 5 and B = 6. The maximum possible value of M is 1.
    Suppose A = 5 and B = 7. The maximum possible value of M is 2.
    Suppose A = 5 and B = 8. The maximum possible value of M is 3.
    Suppose A = 5 and B = 9. The maximum possible value of M is 4.
.
.
.
So on.

It is easy to observe that the maximum value equals the absolute difference between A and B.


    TC: O(1)
    SC: O(1)