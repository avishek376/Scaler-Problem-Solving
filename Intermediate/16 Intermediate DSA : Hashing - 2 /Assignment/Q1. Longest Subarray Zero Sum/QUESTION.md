Problem Description

Given an array A of N integers.
Find the length of the longest subarray in the array which sums to zero.

Note :
while we A[i] multiple times, it may cross the range of integer, so wisely select data type for any operations.



Problem Constraints
    
    1 <= N <= 105
    -109 <= A[i] <= 109


Input Format

Single argument which is an integer array A.


Output Format

Return an integer.

    
    Example Input
    
    Input 1:
    A = [1, -2, 1, 2]

    Input 2:
    A = [3, 2, -1]
      
    Example Output
    
    Output 1:
    3
    Output 2:
    0


Example Explanation

Explanation 1:


 [1, -2, 1] is the largest subarray which sums up to 0.

Explanation 2:

 No subarray sums up to 0.