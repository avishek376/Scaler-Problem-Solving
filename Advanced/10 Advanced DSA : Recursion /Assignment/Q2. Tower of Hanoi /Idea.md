The minimum number of moves to solve the problem with A disks is 2A - 1.
We can find the optimal solution using recursion easily.

We derive the solution intuitevly from 2 disks.
For 2 disks, the move sequence is:
[1, 1, 2]
[2, 1, 3]
[1, 2, 3]

We generate the solution consider the whole stack of A disks into 2 parts: 1, A - 1.
And derive the recursive solution from there.

Pseudocode:

moveDisks(int n, Tower origin, Tower destination, Tower buffer) {

    // Base case
    if (n <= 0) return;

    // move top n - 1 disks from origin to buffer, using destination as a buffer.
    moveDisks(n - 1, origin, buffer, destination);

    // move top from origin to destination
    moveTop(origin, destination);

    // move top n - 1 disks from buffer to destination, using origin as a buffer.
    moveDisks(n - 1, buffer, destination, origin);
}

Refer to the complete solution for more details.


    TC: (N^2)
    SC :O(N)