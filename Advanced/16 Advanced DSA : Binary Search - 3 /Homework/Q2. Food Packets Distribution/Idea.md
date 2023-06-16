If we allot x offices to a city, then a[i]/x number of people can go to a single office.

Hence, for checking if a given number of people can go to a single office, we can add a[i]/x for all cities and check if it is greater than B.

Observe that the answer is monotonic, So we can binary search for the answer.

Check for 0 explicitly.

    
    TC: O(NlogN)
    SC: O(1)