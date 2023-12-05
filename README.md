# LoveLocal-assignment-hard3
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

step 1 -> Function Definition: This function takes an integer n as input and calculates the count of digit '1' in the numbers from 1 to n.

step 2 -> Initialization: Initialize variables count to keep track of the total count of digit '1', factor to represent the place value, and i to iterate through the digits.

step 3 -> Looping through Digits:

The while loop iterates through each digit place from right to left.

divisor represents the next power of 10.

The formula (n // divisor) * i + min(max(n % divisor - i + 1, 0), i) calculates the count of digit '1' at the current place value and adds it to the total count.
      
step 4 -> Return Count: The function returns the total count of digit '1' in the numbers from 1 to n.

step 5 - >Taking User Input: Take s user input for a number (n1).

step 6 -> Printing Result: Calls the count_digit  function with the user-provided number and prints the result.

Example 1:

Input: n = 13

Output: 6

Example 2:

Input: n = 0

Output: 0
