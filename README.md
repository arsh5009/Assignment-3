Task 1 Explaination
•	Defines a function called factorial that takes one argument n.
•	Factorial is only defined for non-negative integers.
•	If the user enters a negative number, the function returns an error message instead of trying to calculate it.
•	Base case: By definition,
o	0! = 1
o	1! = 1
•	If n > 1, we calculate factorial using a loop.
•	result *= i means keep multiplying result by each number from 2 up to n.
•	Example for n = 5:
•	Asks the user for input and converts it to an integer (int).
•	If the user types a non-integer (like "abc"), the program catches the error (ValueError) and prints a friendly message.
•	Otherwise, it calls the factorial function and prints the result.


Task 2 Explaination
•	We import the math module, which provides mathematical functions like square root, logarithm, sine, etc.
•	The program asks the user to enter a number.
•	input() returns a string, so we convert it to float (to allow decimals, e.g., 5.5).
•	Wrapped in try: to handle invalid input (like letters).
•	math.sqrt(x) computes √x.
•	Square root is not defined for negative numbers in real numbers, so we add a check.
•	math.log(x) computes the natural logarithm (log base e).
•	Logarithm is not defined for 0 or negative numbers, so we handle that case.
•	math.sin(x) computes the sine of x, where x is in radians (not degrees).
•	Example: if number = π/2 ≈ 1.57, sin(π/2) = 1.
•	Results are displayed using f-strings for neat formatting.
•	If the user enters something invalid (like "abc"), the program catches the error and prints a friendly message instead of crashing.

