Let's optimize using the fact that the value is up to 106, 
and using the modulo operator, we can reduce all the elements in the range 0 to B-1.

We make an auxiliary array cnt, the index i denotes the number of elements 
which gives i as the remainder when divided by B.

Now, we know that the sum of the pair modulo B should be equal to 0.
So we will count the pairs that give the sum of the pair modulo B is 0.
We can do this by adding cnt[i]*cnt[j] in the answer such that (i + j)%B=0. 

Note: Keep in mind the base case when i==0 and j==0 and i==j.

    TC: O(N)+O(B)
    SC: O(B)