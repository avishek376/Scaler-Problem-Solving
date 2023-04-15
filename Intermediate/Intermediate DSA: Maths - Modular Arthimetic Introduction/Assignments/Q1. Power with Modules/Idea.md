We will have to find the value of (A ^ B) % C.
We initialize our result with 1 and then traverse 
a loop B times and multiply A to our result everytime.
We keep doing modulo C in every step to prevent overflow.

    TC : O(B)
    SC : O(1)