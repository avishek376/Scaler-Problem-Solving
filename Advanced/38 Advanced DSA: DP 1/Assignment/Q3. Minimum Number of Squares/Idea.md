It is always possible to represent a number N as sum of squares i.e.(1^1+1^1+1^1+…..+1^1, N times).
For optimality idea is simple take list of all perfect square numbers ≤ N(i.e. 1,4,9,16….). Now identify from which number we have to make a direct jump to N so that the required answer is minimised.

Take an example of 12 :
List of perfect square numbers ≤12 is 1,4,9.
11+1 = 12, 8+4 = 12, 3+9 = 12.
So to reach 12 we have 3 choices i.e. 11,8,3.

Similarly we will solve for these subproblems with base case as for N=0, ans=0 and for N=1, ans=1.

Hence we can write required recursion as follows :
    
    If n <= 1, 
    then return n 
    Else
       countMinSquares(n) = min {1 + countMinSquares(n - i*i)} 
                           where i >= 1 and i*i <= n
We can easily transform this exponential solution to DP as below :

    dp[0]=0,dp[1]=1; // base cases.
    i : [2...N]
    {
        dp[i]=i;
        for every x : x>=1 & x*x<=i
        {
            dp[i]=min(dp[i],1+dp[i-x*x]);
        }
    }

    TC : O(N*sqrt(N))
    SC : O(N)