We will sort the items by there A[i] / B[i] ratio or (value / weight) ratio
in descending order. Then we keep choosing the first element till our knapsack
is not filled. The last item maybe be present in fractional amount.

    TC : O(NlogN)
    SC : O(N)