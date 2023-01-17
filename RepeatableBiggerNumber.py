'''
Repeatable Bigger Number
1/16/2023
Python I

Instructions:
Trace the program and predict what it will display.
Then run the program to check your work. Finally, be
prepared to discuss the following questions...
1. Based on this example, can a while loop contain an if statement?
2. What is the purpose of this line of code?
   repeat = input("Would you like to enter 2 different numbers? (Y/N) >> ")

3. What does this line of code do? Why did Mr. Pawelski include this
   line of code in the program?
   print()

4. What does the user need to enter for the program or loop to repeat?

'''

repeat = "Y"
while repeat == "Y" or repeat == "y":
    num1 = int(input("Enter a number >> "))
    num2 = int(input("Enter another number >> "))
    if num1 < num2:
        print(str(num2) + " is bigger than " + str(num1))
    elif num2 < num1:
        print(str(num1) + " is bigger than " + str(num2))
    else:
        print("The numbers are the same.")

    # Checks if the program should repeat
    repeat = input("Would you like to enter 2 different numbers? (Y/N) >> ")
    print()
