Initially, sort the array in ascending order.
For the minimum magic, find the sum of the difference between adjacent elements in pairs of two.
    
    for i=1 ; i<n ; i+=2
        min_magic+=a[i]-a[i-1]
For the maximum magic, find the sum of the difference between the two elements equidistant from the front and back of the array.
    
    for i=0 ; i<n/2 ; i++
        max_magic+=a[n/2+i]-a[i]



    TC: O(NlogN)
    SC: O(1)


