Very simple simulation problem. Just need to keep track of the digits seen in every row, every column and every block as defined in the rules.
Whenever you encounter a digit already seen, you know the sudoku is not valid.

Note that this problem will get very complicated if you were to determine if the sudoku was solvable.

    
    TC :O(1)
    SC :O(1)