We will count the distinct number of factors of each element.
Then we will sort the array using comparator function.
In the comparator function we will first calculate the number
of factors if each of the two numbers. If this count is equal, 
then the smaller number will come first. Otherwise, the number
with the least number of factors will come first.

    TC: O(N*logN*√A[i])
    SC : O(1)