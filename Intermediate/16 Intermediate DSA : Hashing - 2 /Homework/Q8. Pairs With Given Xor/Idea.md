A Simple solution is to traverse each element and check if there’s another number whose XOR with it is equal to B.
This solution takes O(N2) time.

The efficient solution to this problem takes O(N) time.
The idea is based on the fact that A[i] ^ A[j] is equal to B if and only if A[i] ^ B is equal to A[j].

Initialize the result as 0.
Create an empty hash set “s”.
Do the following for each element A[i] in A[]
If B ^ A[i] is in “s”, then increment the result by 1.
Insert A[i] into the hash set “s”.
Return result.

    
    TC :O(N)
    SC :O(N)