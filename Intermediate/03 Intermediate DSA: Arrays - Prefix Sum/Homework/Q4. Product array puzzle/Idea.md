We will have a prefix array pref[] where pref[i] will store the 
multiplication of all the elements in the prefix of the array till
i-th position. Similar we will have a suffix array suff[].
Now for the i-th element, we can find the multiplication of all the 
elements to it's left from the pref[] array and that in the right side
from the suff[] array

    TC : O(N)
    SC : O(N)