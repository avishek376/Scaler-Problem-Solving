Approach:

There are two steps:
1. Create cumulative sum array where ith index in this array represents total sum from 1 to ith index element.
2. Iterate all elements of cumulative sum array and use hashing to count two elements where value at ith index == value at jth index but i != j.
3. IF element is not present in hash in fill hash table with current element.


TC : O(N)
SC : O(N)