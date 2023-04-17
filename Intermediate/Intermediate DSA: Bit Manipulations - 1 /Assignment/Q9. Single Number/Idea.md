XOR will return 1 only on two different bits. So if two numbers are the same, XOR will return 0.

Finally, there is only one number left.

A ^ A = 0 and A ^ B ^ A = B.

So, all the even occurrences will cancel out using XOR.

    TC : O(N)
    SC : O(1)