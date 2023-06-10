We observe that the number of time a door X alter its state is the number of factors of that door X.
If the number of factors is even, then the door will be closed; else, it will be open.

So, we need to find the numbers between 1 to A for which the number of factors is odd.

This leads to a very interesting observation that only the number which is perfect square has an odd number of factors.
How?
If ‘a’ is a factor of ‘X’, then there will be a ‘b’ such that ‘a’ * ‘b’ = X.
Only a number that is perfectly square has a factor ‘a’ such that ‘a’ * ‘a’ = X.

So we will count the number of perfect squares between 1 and A, and that will be sqrt(A).


    TC: O(LogA)
    SC: O(1)