Note the following :

Let G(n) represent a gray code of n bits.
Let R(n) denote the reverse of G(n).

Note that we can construct.
G(n+1) as the following :
0G(n)
1R(n)

Where 0G(n) means all elements of G(n) prefixed with 0 bit and 1R(n) means all elements of R(n) prefixed with 1.
Note that the last element of G(n) and the first element of R(n) are the same. So the above sequence is valid.

Example G(2) to G(3) :

    0 00
    0 01
    0 11
    0 10
    1 10
    1 11
    1 01
    1 00


    
    TC: O(2^N)
    SC: O(N)