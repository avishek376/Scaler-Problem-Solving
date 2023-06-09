We can try to remove the common factors of A and B from A by finding the greatest common divisor (gcd) of A and B and dividing A with that gcd.

Mathematically, A = A / gcd(A, B) —— STEP1
Now, we repeat STEP1 till we get gcd(A, B) = 1.
Atlast, we return X = A

How does this work ?

On doing prime factorization of A and B, we get :

A = p1x1 . p2x2 . … . pkxk
B = q1y1 . q2y2 . … . qlyl
Where pi ; i = 1, 2, …, k are prime factors of A and xi ; i = 1, 2, …, k are their respective powers
Similarly, qj ; i = 1, 2, …, l are prime factors of B and yi ; j = 1, 2, …, l are their respective powers

Let ri ; i = 1, 2, …, m be the common factors of A and B. By repeating STEP1, we are reducing the respective powers of ri by at least one each time (Proof of this is left to the reader). Therefore, we reach a point where powers of ri become zero, and the product of the rest prime-powers in A form the largest divisor of A that is co-prime with B.

    TC: O( log(max(A,B) )* logA)
    SC: O(1)