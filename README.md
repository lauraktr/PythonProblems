# FizzBuzz

## Instructions

1. Declare a function called fizzbuzz() that take one of the following parameters:
    * A number that is an integer value
    * An array of integer values
   
    and returns one of the following objects:
    
    * An integer or string
    * An array of integers and/or strings
    
2. If the number is divisible by 3, return "Fizz"

3. If the number is divisible by 5, return "Buzz"

4. If the number is divisible by 5 and 3, return "FizzBuzz"

5. If the number is not divisible by 3 or 5, return the number

6. You may use the following test cases:
    
    a. Integers
    
        6  --> "Fizz"
        30 --> "FizzBuzz"
        27 --> "Fizz"
        45 --> "Buzz"
        97 --> 97
    
    b. Arrays
    
         [5, 16, 18, 99, 47, 6, 33]  --> ["Buzz", 16, "Fizz", "Fizz", 47, "Fizz", "Fizz"]
         [1, 2,  3,  4,  5,  6,  7]  --> [1, 2, "Fizz", 4, "Buzz", "Fizz", 7]
         [5, 10, 15, 20, 25, 30, 35] --> ["Buzz", "Buzz", "FizzBuzz", "Buzz", "Buzz", "FizzBuzz", "Buzz"]
    
    
# Blanks

## Instructions

1. Declare a function called blanks() that will take the following parameters:
   
    * a 2D array
    * two integer numbers
    
    and returns:
    
    * an array of indices
    * a boolean
    
2. Scan the 2D array and create an array with the indices of all blank (" ") elements

3. Create a boolean variable that is true if the index created by the given integers is blank and is false if it is 
not blank

4. You may test with the following cases:


       [["s", "m" ," ", "h"],
        ["h", " ", " ", "s"],      ---------->    [2, 5, 6, 9], False         
        ["m", " ", "m", "m"]], 4  
       
       
   and
       
       
       [[" ", " ", "r"],          ----------->    [0, 1, 3, 4], True
        [" ", " ", "p"]], 0
    
    
# Frequency

## Instructions

1. Declare a function called frequency() that will take the following parameters:
   
    * An array of integers
    * An integer
    
    and will return:
    
    * an integer 
    
2. Scan the array and count the number of times the given integer occurs in the array

3. Return and integer containing the frequency

4. You may test with the following cases:

        [1, 5, 2, 3, 3, 1, 3], 3           --> 3
        [9, 6, 2, 8, 7, 2, 4, 4, 1, 6], 6  --> 2
        [7, 5, 4, 1, 5, 2, 2, 1, 5], 7     --> 1
    
    
# Snakes

Declare a function called ends() that will take a 2D matrix and count the number 
of line ends present. You may assume the board is always 4 dots wid and 3 dots tall.

For example:

    [[" ", "_", "_"],
     ["|", " ", " ", "|"],
     [" ", " ", " "],
     ["|", " ", " ", " "],
     [" ", " ", " "]]
     
would print as:

    . ._._.
    |     |
    . . . .
    |      
    . . . .
     
would have 4 ends, while 
    
    [["_", "_", "_"],
     ["|", " ", " ", "|"],
     [" ", " ", " "],
     ["|", " ", " ", " "],
     [" ", " ", " "]]
     
would print as

    ._._._.
    |     |
    . . . .
    |      
    . . . .
    
and have 2.

# Dots and Boxes

Declare a function called complete_box(), which takes a 2D array and counts the number of completed boxes.  You may 
assume the board is always 4 dots wid and 3 dots tall.

For example:

    [["_", "_", "_"],
     ["|", "|", " ", "|"],
     ["_", " ", " "],
     ["|", " ", " ", " "],
     [" ", " ", " "]]
     
would print as:

    ._._._.
    | |   |
    ._. . .
    |      
    . . . .
     
would have 1 completed box, while 
    
    [["_", "_", "_"],
     ["|", "|", "|", "|"],
     ["_", "_", "_"],
     ["|", "|", " ", " "],
     ["_", " ", " "]]
     
would print as:

    ._._._.
    | | | |
    ._._._.
    | |    
    ._. . .
    
and have 4.


# Connect 4

Declare a function add_to_column() which takes a 2D array, a column number, and a character (R, B). It stacks a 
character on top of that column and returns the new 2D array. You may assume the array is 5 by 5.

For example:

    [[" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", "B", "R", " ", " "],
     ["R", "B", "B", "R", " "]], 3, "R"
     
would return:

    [[" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", "B", "R", "R", " "],
     ["R", "B", "B", "R", " "]]
    
and this:

    [[" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", "B", "R", " ", " "],
     ["R", "B", "B", "R", " "]], 0, "B"
     
would return:

    [[" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     ["B", "B", "R", " ", " "],
     ["R", "B", "B", "R", " "]]
     
     
# Battleship

Declare a function called place_ship() which takes a 2D array, an integer, and a character (L, R, U, D). It will add a 
ship of length 3, starting at the given index and going in the given direction. You may assume the array is 5 by 5.

For example:

    [["S", " ", " ", " ", " "],
     ["S", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "]], 15, "R"
     
would return:

    [["S", " ", " ", " ", " "],
     ["S", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     ["S", "S", "S", " ", " "],
     [" ", " ", " ", " ", " "]]
    
and this:

    [[" ", " ", " ", " ", " "],
     [" ", " ", " ", "S", "S"],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "]], 0, "D"
     
would return:

    [["S", " ", " ", " ", " "],
     ["S", " ", " ", " ", " "],
     ["S", " ", " ", "S", "S"],
     [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "]]


