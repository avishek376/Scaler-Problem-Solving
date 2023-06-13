The idea is to use Merge function of Merge sort.

Let n1 = A.size() and n2 = B.size()
1)Create an array arr[] of size n1 + n2.
2)Simultaneously traverse A[] and B[].
3)Pick smaller of current elements in A[] and B[], copy this smaller element to next position in arr[] and move ahead in arr[] and the array whose element is picked.
4)If there are remaining elements in A[] or B[], copy them also in arr[]

    TC: O(n1 + n2)
    SC: O(n1 + n2)