We will keep the count of frequency of each of the
elements of the array using a frequency array. Then
we will move from 1 to size of the the frequency array
and insert them in our final sorted array.



    TC : O(N + K)
    SC : O(K)
    where N is the size and K is the maximum 
    value of the given array


**Approach-2**

 1)for this I used an index array upto max elemnt of A not 10**5 to save time
              
 2)created an index array starting from 0 upto max elemnt as end
 3)here whatever be element of A its index  will get its total count\
 4)picks element one by one
 5)in ans array the value of index * single elemnt array =[el,el,el,...(upto its value in index)]

    The given solution is based on this approach

    TC: O(N+K)
    SC: O(K)

