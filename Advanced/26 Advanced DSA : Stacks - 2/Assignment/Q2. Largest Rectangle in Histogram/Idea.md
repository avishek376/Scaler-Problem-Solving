We already know from our previous observation that when I traverse left, I only need entries in decreasing order.

We traverse all histograms from left to right and maintain a stack of histograms. Every histogram is pushed to stack once. A histogram is popped from the stack when a histogram of smaller height is seen. We calculate the area with the popped histogram as the smallest histogram when a histogram is popped. How do we get left and right indexes of the popped histogram – the current index tells us the ‘right index’ R, and the index of the previous item in the stack is the ‘left index’ L. Following is a rough pseudocode.

    max_rectangle = 0
    stack = an instance of empty stack
    for index = 0 to all_histograms.length
        if stack.empty OR H[index] > H[stack.top]
            Push index to the stack
        if H[index] < H[stack.top]
            while !stack.empty && H[stack.top] > H[index]
                h = H[stack.pop]
                # Calculate the area with h as the smallest height. 
                R = index
                L = stack.top
                max_rectangle = MAX(max_rectangle, (R - L - 1) * h)
            Push index to the stack
    if stack is not empty
Repeat removing entries one by one from the stack and calculating the max_rectangle as done earlier.

TC: O(N)
SC: O(N)