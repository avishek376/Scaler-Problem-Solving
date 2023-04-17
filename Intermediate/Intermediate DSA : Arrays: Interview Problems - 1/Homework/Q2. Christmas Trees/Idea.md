To solve this, let’s take three indices, p, q and r.

p is the index of the tree that is to be chosen first, i.e. the one with the smallest height.
q is the index of the tree that is to be chosen second, i.e. the one with the middle height.
r is the index of the tree that is to be chosen third, i.e. the one with the largest height.
We should now traverse the array by fixing index q. Lets N be the size of the array.

For q, that goes from index q+1 to N-1, we can find an index p that goes from 1 to q-1 such that A[p] < A[q], and B[p] is minimum.
Similarly, find an index r that goes from q+1 to N such that A[r] > A[q], and B[r] is minimum.

This way, for all q we can find the minimum values, and we choose the minimum values from all the q values.

    TC : O(n^2)
    SC : O(1)