# Lab_3
# Lab_3
Aim of the Lab
To develop a clear understanding of control structures in Python by implementing conditional statements,
loops, break and continue statements, and to learn how to define and invoke functions for solving
programming problems in a structured and efficient manner.

List of programs :
1. To check if the number is Positive, Negative, or Zero.
It demonstrates the use of conditional statements (if, elif, else).  

- It starts by asking the user to input a number using input().  
- The number is converted from a string to an integer with int().  
- Then, the program checks the value of the number:  
- If the number is greater than 0, it prints "positive".  
- If the number is equal to 0, it prints "zero".  
- Otherwise (meaning the number is less than 0), it prints "negative".

2. To check whether the number is even or odd.
  input("Enter a number: ")
   - This line asks the user to type something in.
   - Whatever the user types is taken as a string by default.
 int(...)
   - The int() function converts that string into an integer.
   - Example: if you type 7, it becomes the integer 7.
 n % 2 == 0
   - % is the modulus operator. It gives the remainder when dividing n by 2.
   - If a number is divisible by 2 (remainder = 0), it’s even.
   - If the remainder is not 0, it’s odd.
 if ... else ...
   - This is a conditional statement.
   - If the condition (n % 2 == 0) is true, it prints "The number is even."
   - Otherwise, it prints "The number is odd."

3. To find the largest of two numbers. 
- Define functions for add, subtract, multiply, divide.  
- Use while True to repeat menu.  
- Perform chosen operation.  
- Exit when user selects 5.  

4. Largest of Three numbers 
Largest of Three Numbers (nested if-else)
Use nested if-else statements. First compare two numbers, then compare the winner with the third. This ensures you check all possibilities step by step.
- Input three numbers.  
- First compare a and b.  
- Then compare the larger one with c.  
- Nested if-else ensures you check all cases.  

5. Display Grade Based on Marks
Use if-elif-else. Compare the input marks against ranges (≥80 → A, 60–79 → B, 40–59 → C, <40 → Fail). Print the grade accordingly.
- Input marks.  
- Use if-elif-else to check ranges:  
  - ≥80 → A  
  - 60–79 → B  
  - 40–59 → C  
  - <40 → Fail  

6. Menu-Driven Calculator
Show a menu with choices. Use if-elif to decide which operation to perform. Take two inputs, perform the chosen operation, and handle division carefully by checking denominator ≠ 0.
- Show menu with choices.  
- Use if-elif to decide operation.  
- Take two numbers.  
- Perform chosen operation.  
- For division, check num2 != 0 to avoid error.  


7. Print Numbers 1 to 10 (for loop)
Use a for loop with range(1, 11). Print each number in sequence.
- Use for i in range(1, 11).  
- Print each number.

8. Print Even Numbers 1 to 20
Use a for loop with step size 2 (range(2, 21, 2)). Print each value.
- Use for i in range(2, 21, 2).  
- Prints only even numbers.

9. Sum of First 10 Natural Numbers
Initialize a variable sum = 0. Use a loop from 1 to 10, add each number to sum. Print the result.
- Initialize sum = 0.  
- Loop from 1 to 10.  
- Add each number to sum.  
- Print result.

10. Multiplication Table
Take a number as input. Use a for loop from 1 to 10. Multiply the number by the loop counter and print in table format.
- Input a number.  
- Loop from 1 to 10.  
- Multiply number by loop counter.  
- Print in table format.

11. Print Numbers 1 to 5 (while loop)
Initialize i = 1. Use while i <= 5. Print i and increment by 1 each time.
- Start with i = 1.  
- While i <= 5, print i.  
- Increment i each time.  


12. Sum from 1 to n (while loop)
Take n as input. Initialize sum = 0 and i = 1. Use while i <= n, add i to sum, increment i. Print final sum.
- Input n.  
- Initialize sum = 0, i = 1.  
- While i <= n, add i to sum.  
- Increment i.  
- Print sum.

13. Keep Taking Input Until 0
Use an infinite loop (while True). Take input each time. If input equals 0, break the loop and print “Loop ended”.
- Use while True.  
- Input number each time.  
- If number == 0 → break loop.  
- Print “Loop ended”.  


14. Stop at 6 (break)
Use a for loop from 1 to 10. If the number equals 6, use break. Otherwise, print the number. 
- Loop from 1 to 10.  
- If number == 6 → break.  
- Otherwise print number.

15. Skip 5 (continue)
Use a for loop from 1 to 10. If the number equals 5, use continue to skip printing. Otherwise, print the number.
- Loop from 1 to 10.  
- If number == 5 → continue (skip).  
- Otherwise print number.  


16. Search Number in List (break)
Loop through the list. If the current element equals the search number, print “Found” and break. If loop ends without finding, print “Not found”.
- Loop through list.  
- If element == search → print “Found” and break.  
- If not found after loop → print “Not found”.

17. Function to Print Hello World
Define a function with def. Inside, print “HELLO, WORLD”. Call the function.
- Define function with def.  
- Inside, print “HELLO, WORLD”.  
- Call the function.

18.  Function to Return Square
Define a function that takes a number and returns num * num. Call the function with user input and print the result.
- Define function that returns num * num.  
- Input number.  
- Call function and print result.

19. Function to Add Two Numbers
Define a function with two parameters. Return their sum. Take two inputs, call the function, and print the result.
- Define function with two parameters.  
- Return their sum.  
- Input two numbers.  
- Call function and print result.  

20.  Function to Check Even/Odd
Define a function that checks num % 2 == 0. If true, print “Even”, else print “Odd”.
- Define function.  
- If num % 2 == 0 → even.  
- Else → odd.

21. Function to Calculate Factorial
Define a function. Initialize result = 1. Use a loop from 1 to n, multiply each value into result. Return result.
- Define function.  
- Initialize result = 1.  
- Loop from 1 to n.  
- Multiply each into result.  
- Return result.

22. Function to Print Multiplication Table
Define a function that takes a number. Use a loop from 1 to 10. Print num x i = num*i.
- Define function.  
- Loop from 1 to 10.  
- Print num x i = num*i.

23. Function + Loop to Print Even/Odd up to n
Define a helper function to check even/odd. Use a loop from 1 to n. For each number, call the helper and print result.
- Define helper function to check even/odd.  
- Loop from 1 to n.  
- For each number, call helper and print result.

24.  Menu-Driven Calculator with Loop
Define functions for add, subtract, multiply, divide. Use a while True loop to repeatedly show menu. Perform chosen operation until user selects Exit.3
- Define functions for add, subtract, multiply, divide.  
- Use while True to repeat menu.  
- Perform chosen operation.  
- Exit when user selects 5.  


