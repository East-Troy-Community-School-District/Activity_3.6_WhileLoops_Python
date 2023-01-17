'''
Sum Numbers
1/16/2023
Python I

Instructions:
Trace the program and predict what it will display. Then run the
program to check your work. Finally, be prepared to discuss the
following questions...
1. What does the program do?
2. What is the sentinel value for the while loop?
3. What does the following line of code do in the program?
   total = total + number

   In this program, total is an example of an accumulator variable.
   An accumulator variable is a variable that is used to calculate
   a sum or product of a series of values. In this program, it
   finds the sum of all the numbers entered by the user.
4. Is there another way to write line 27?
'''

total = 0
print("Enter numbers to find the sum. Enter -1 when finished.")
number = int(input("Number >> "))
while number != -1:
    total = total + number
    number = int(input("Number >> "))
print("The sum is " + str(total))