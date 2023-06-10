Here we should not use Sieve Algorithm .

The reason behind this is we are given the constraints as following:
    1 <= N <= 1e3
    
    1 <= A[i] <= 1e6
    now if you use sieve approach then your time complexity will depends upon A[i] which can go atmost 10^6. 
    But if you use simple approach where you will simply check every number in the array is prime or not then your complexity would depend upon size of the array and log of A[i]( As we can check if num is prime or not in log(n) time).
    So Brute force Approach would have TC = O(N*log(A[i]) where as Sieve Algorithm Approach would have TC of O(A[i] * log(log(A[i])).
    Due to which you would definitely get TLE. so better to use brute force approach.


    TC: O(NlogN)
    SC: O(1)