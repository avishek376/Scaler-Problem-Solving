There are two important things to note here:

1) Overflow situation: Note that if x is large enough, multiplying x to the answer might overflow in integer.

2) Multiplying x one by one to the answer is O(n). We are looking for something better than O(n).

If n is even, note the following:

x ^ n = (x * x) ^ n/2

    TC :O(N)
    SC :O(N)