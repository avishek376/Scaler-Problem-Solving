So when is a number prime? When it is not divisible by any integer other than 1 and itself.
Now to check if a number is prime or not till which number should we check and see if it divides our number N?
Should we check till N-1? or should we check till N/2. or could we check even less numbers? 
Remember the lesser numbers we check the faster our program will be.

Well the right answer is we can confirm if the number is prime or not by checking upto the numbers floor(sqrt(N)).
Think why this is true.

    
    TC: (sqrt(N))
    SC: O(1)