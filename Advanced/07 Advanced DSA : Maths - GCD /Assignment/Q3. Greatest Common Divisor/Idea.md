Let's say g is gcd(m, n) and m > n.

m = g * m1
n = g * m2

m - n = g * (m1 - m2)

    gcd (m, n) = gcd(m-n, n)

           = gcd(m - 2n, n) if m >= 2n
           = gcd(m - 3n, n) if m >= 3n 
             .
             .
             .
           = gcd(m - k*n, n) if m >= k*n

       In other words, we keep subtracting n till the result is greater than 0. Ultimately we will end up with m % n.

              So gcd(m, n)  = gcd(m % n, n) 



    TC: O( log( min(a,b) )
    SC: O( log( min(a,b) )