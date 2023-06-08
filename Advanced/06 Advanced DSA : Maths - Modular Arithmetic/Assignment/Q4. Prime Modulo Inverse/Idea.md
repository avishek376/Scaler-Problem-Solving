**Fermats’s little theorem:**

AB-1 ≡ 1 (mod B) where B is prime and A is not a multiple of B.

Multiply by A-1 on both sides, We get

AB-2 ≡ A-1 (mod B) where B is prime and A is not a multiple of B.

We just have to calculate AB-2 (mod B). This will be the modular multiplicative inverse of A under modulo B.

    TC: O(logN)
    SC: O(logN)