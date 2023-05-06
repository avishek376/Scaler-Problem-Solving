We will find the tens digit of each element by dividing by 
10 and then finding the mod of 10 of that value.
Then we will sort the array using comparator function.
In the comparator function we will first find the tens digit
of the two numbers. If this digit is equal, then the larger number 
will come first. Otherwise, the number with the least tens digit 
will come first.

    TC : O(N*logN)
    SC : O(1)