Here we will solve what has been discussed in the previous hint :

Problem statement: Given a fixed number of pages (V),  how many students do we need?
The problem has the following property, if it the maximum of minimum value of pages allocated to a student is <= V then it is always
possible to allocate X as the maximum of minimum pages allocated to a student such than X>=V.

This leads us to a binary search solution. 



Solution :
```       simple simulation approach
       intially Sum := 0
       cnt_of_student = 0
       iterate over all books:
            If Sum + number_of_pages_in_current_book > V :
                      increment cnt_of_student
                      update Sum
            Else:
                      update Sum
       EndLoop;
    
```

    fix range LOW, HIGH
    Loop until LOW < HIGH:
            find MID_point
            Is the number of students required to keep the max number of pages below MID < M? 
            IF Yes:
                update HIGH
            Else
                update LOW
    EndLoop;

    
    TC: O(NlogN)
    SC: O(1)
