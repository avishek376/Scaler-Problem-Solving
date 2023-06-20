1) Loop through A, store the count of every number in a HashMap (key: number, value: count of number).
2) Loop through B, check if it is present in HashMap, put in the output array as many times in A,
and remove the number from HashMap.
3) Sort the rest of the numbers in HashMap and put them in the output array

Instead of HashMap use OrderedMap.

    TC: O(N)
    SC: O(N)