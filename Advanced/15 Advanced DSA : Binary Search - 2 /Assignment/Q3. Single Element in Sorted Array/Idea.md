Lets say the position of the element occuring once is x.
What property do you observe for the elements which are towards the left of x?

For any i from [0,x) ,we can say that

    if i is even A[i]==A[i+1]
    if i is odd  A[i]==A[i-1]
This cannot be said for elements from [x+1,n). Because in that case if i is even A[i]==A[i-1] and vice versa.

Therefore we just have to find the last index ‘j’ such that it satisfies the property of index from [0,x).
If we get j , then A[j+1] would be our answer.


    TC: O(logN)
    SC: O(N)