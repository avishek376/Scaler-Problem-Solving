If the two points are (x1, y1) and (x2, y2), then their slope will be (y2 – y1) / (x2 – x1),
which can be a double value and can cause precision problems.

To get rid of the precision problems, we treat slope as pair ((y2 – y1), (x2 – x1)) instead of ratio and reduce pair by their gcd before inserting into the map.

Points that are vertical or repeated are treated separately.

Note: If we use a map in C++ or HashMap in Java for storing the slope pair, then the total time complexity of the solution will be O(n^2 logn)


    TC: O(N^2 logN)
    SC: O(N)