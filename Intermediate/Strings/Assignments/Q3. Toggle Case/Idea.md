For every character in A:

If A[i] is uppercase, we can change it to 'a' + (A[i]-'A')
If A[i] is lowercase, we can change it to 'A' + (A[i]-'a')

Difference between ASCII value of "A" and "a" is 32 => 2^5=> 1<<5
So, add if you want A->a
else
subtract to get a->A