Efficient Approach using Merge Sort

Suppose we know the number of inversions in the left half and the right half of the array, lets call them inv_l and inv_r.
Which inversions are not counted in inv_l+inv_r ? The elements in the left half which are greater than the elements in the right half. These are the inversions which are not counted.

Lets assume that both left half and right half are sorted. Can we count the number of inversions now?
We can just merge the two arrays and whenever we find that a[i] > a[j] (where i is the pointer of left half of the array and j is the pointer of the right half of the array) we simply increment the number of inversions.
The final answer will be inv_l + inv_r + number of inversions found during merge step.

Does this remind of a famous algorithm?

Yes, thats right. It is Merge Sort with a slight modification

    TC: O(NlogN)
    SC: O(N)