Problem Description

Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j].
Return the number of important reverse pairs in the given array A.



Problem Constraints

    1 <= length of the array <= 105
    
    -2 * 109 <= A[i] <= 2 * 109



Input Format

The only argument given is the integer array A.



Output Format

Return the number of important reverse pairs in the given array A.



Example Input

    Input 1:
    
     A = [1, 3, 2, 3, 1]
    
    Input 2:
    
     A = [4, 1, 2]
    
    
    Example Output
    
    Output 1:
    
     2
    
    Output 2:
    
     1


Example Explanation

Explanation 1:

 There are two pairs which are important reverse pair 
    
     i.e  (1, 4) => A[1] > 2 * A[4] => 3 > 2 * 1 => 3 > 2 and
          (3, 4) => A[3] > 2 * A[4] => 3 > 2 * 1 => 3 > 2.

Explanation 2:

 There is only one pair 
    
     i.e (0, 1) => A[0] > 2 * A[1] => 4 > 2 * 1 => 4 > 1