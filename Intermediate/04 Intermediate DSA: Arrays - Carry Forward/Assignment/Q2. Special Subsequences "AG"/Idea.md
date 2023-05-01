We can instead keep a variable ‘g’ storing count of G’s and iterate in the reverse order.
If the current character is ‘G’ , increment g.
If the current character is ‘A’ , add g to our answer.

    for i from n-1 to 0
        if A[i]=='G'
            g++
        else 
            ans+=g
            ans%=mod
    
    TC : O(n)
    SC : O(1)