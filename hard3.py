#Function Definition:This function takes an integer n as input and calculates the count of digit '1' in the numbers from 1 to n.
def count_digit(n):
    #Initialization:Initialize variables count to keep track of the total count of digit '1', factor to represent the place value, and i to iterate through the digits.
    count = 0
    factor = 1
    i = 1
    #Looping through Digits:The while loop iterates through each digit place from right to left.
    while i <= n:
        divisor = i * 10 #divisor represents the next power of 10.
        count += (n // divisor) * i + min(max(n % divisor - i + 1, 0), i)  #The formula (n // divisor) * i + min(max(n % divisor - i + 1, 0), i) calculates the count of digit '1' at the current place value and adds it to the total count.
        i *= 10

    return count #Return Count:The function returns the total count of digit '1' in the numbers from 1 to n.
#Taking User Input:Takes user input for a number (n1).
n1 = int(input("enter a number"))
#Printing Result:Calls the count_digit  function with the user-provided number and prints the result.
print(count_digit(n1)) 

