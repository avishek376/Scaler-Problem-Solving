If we observe bits from rightmost side at distance i than bits get inverted after 2i position in vertical sequence.

For example A = 5;
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101

So, we will iterate till the number of bits in the number. And we don’t have to iterate every single number in the range from 1 to A.
We will perform the following operations to get the desired result.

First of all, we will add 1 to the number in order to compensate 0. As the binary number system starts from 0. So now A = A + 1.
We will keep the track of the number of set bits encountered till now. And we will initialise it with A/2.
We will keep one variable which is a power of 2, in order to keep track of bit we are computing.
We will iterate till the power of 2 becomes greater than A.
We can get the number of pairs of 0s and 1s in the current bit for all the numbers by dividing A by current power of 2.
Now we have to add the bits in the set bits count. We can do this by dividing the number of pairs of 0s and 1s by 2 which will give us the number of pairs of 1s only and after that, we will multiply that with the current power of 2 to get the count of ones in the groups.
Now there may be a chance that we get a number as number of pairs, which is somewhere in the middle of the group i.e. the number of 1s are less than the current power of 2 in that particular group. So, we will find modulus and add that to the count of set bits.


    TC : O(logA)
    SC: O(1)