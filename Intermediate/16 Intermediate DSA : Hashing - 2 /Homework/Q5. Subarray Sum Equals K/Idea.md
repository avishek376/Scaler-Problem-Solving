**Approach- 1 (Brute Force)**
The simplest method is to consider every possible subarray of the given numsnums array, find the sum of the elements of each of those subarrays and check for the equality of the sum obtained with the given kk. Whenever the sum equals kk, we can increment the countcount used to store the required result.
Time complexity : O(n^3)
Space complexity : O(1)
***
**Approach- 2 (using cumulative sum)**

Instead of determining the sum of elements every time for every new subarray considered, we can make use of a cumulative sum array , sumsum. Then, in order to calculate the sum of elements lying between two indices, we can subtract the cumulative sum corresponding to the two indices to obtain the sum directly, instead of iterating over the subarray to obtain the sum.

In this implementation, we make use of a cumulative sum array, sumsum, such that sum[i] is used to store the cumulative sum of numsnums array up to the element corresponding to the (i-1)^{th} index. Thus, to determine the sum of elements for the subarray nums[i:j], we can directly use sum[j+1] - sum[i].
Time complexity : O(n^2)
Space complexity : O(n)
***
**Approach- 3 (without space)**

Instead of considering all the startstart and endend points and then finding the sum for each subarray corresponding to those points, we can directly find the sum on the go while considering different endend points. i.e. We can choose a particular startstart point and while iterating over the endend points, we can add the element corresponding to the endend point to the sum formed till now. Whenever the sumsum equals the required kk value, we can update the countcount value. We do so while iterating over all the endend indices possible for every startstart index. Whenever, we update the startstart index, we need to reset the sumsum value to 0.
Time complexity : O(n^2)
Space complexity : O(n)
***
**Approach- 4 (Using Hashmap)**

The idea behind this approach is as follows: If the cumulative sum(represented by sum[i] for sum up to i^{th} index) up to two indices is the same, the sum of the elements lying in between those indices is zero. Extending the same thought further, if the cumulative sum up to two indices, say i and j is at a difference of k i.e. if sum[i] - sum[j] = k, the sum of elements lying between indices i and j is k.

Based on these thoughts, we make use of a hashmap map which is used to store the cumulative sum up to all the indices possible along with the number of times the same sum occurs. We store the data in the form: (sum_i, no. of occurrences of sum_i). We traverse over the array numsnums and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered, we also determine the number of times the sum sum-ksum−k has occurred already, since it will determine the number of times a subarray with sum kk has occurred up to the current index. We increment the count by the same amount.

After the complete array has been traversed, the count gives the required result.

    TC : O(n)
    SC : O(n)