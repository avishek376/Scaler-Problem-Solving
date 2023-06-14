There are many sorting algorithms, but for this problem we will use QuickSort of sort the array.
QuickSort is a Divide and Conquer Algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

There are many different versions of quickSort that pick pivot in different ways:

-> Always pick first element as pivot.
-> Always pick last element as pivot (implemented below)
-> Pick a random element as pivot.
-> Pick median as pivot.

The key process in quickSort is partition().
Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.
All this should be done in linear time.

    Average Case Time Complexity : O(NlogN)
    Worst Case : O(N2)
    SC: O(N)