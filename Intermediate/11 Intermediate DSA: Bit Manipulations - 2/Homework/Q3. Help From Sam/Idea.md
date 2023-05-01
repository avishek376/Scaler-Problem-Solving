Claim :The number of times we would require help from sam is the number of bits that are set in A.

Lets try to build an intuition for this. Instead of going from 0 to A , we will go in the reverse direction i.e. from A to 0.
First initialise a cnt variable to 0 which is the number of times we took help from sam.Now we would follow this approach until A becomes 0.

If A is an even number we can divide it by 2
otherwise if A is an odd number we can subtract 1 from it and increment the cnt.

Since every time we divide by 2 if its an even number , it is same as doing a left shift. The number of times A would become odd is the number of set bits of A.

Lets take an example to make this more clear:

A=17
0) 17 ,cnt=0
1) 17 -> 16 , cnt=1
2) 16 -> 8 , cnt=1
3) 8 -> 4 , cnt=1
4) 4 -> 2 , cnt=1
5) 2 -> 1 , cnt=1
6) 1 -> 0 , cnt=2

binary representation of 17 = 10001 , and we can see that the number of set bits is the same as cnt that we obtained in the above approach.

Therefore it is enough to just find the number of set bits of A.

We can do this as follows:

cnt=0
for i from 0 to 31
    if A&(1<<i) != 0 
        cnt++
return cnt

    TC : O( log(A) )
    SC: O(1)