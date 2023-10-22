'''
Guess My Number
Pawelski
10/22/2023
Introduction to Computer Science

Instructions:
Trace the program and predict what it will display. Then
run the program to check your work. Finally, be prepared
to discuss the following questions...
1. What does the program do?
2. How does the program work? Explain what is happening
   in the program step by step (i.e., what happens first,
   second, third, etc.).
3. What causes the loop to stop?
4. By just looking at the code, can you determine how
   many times the loop will repeat? Why?
'''

import random

mysteryNumber = random.randint(1, 10)
guess = int(input("Guess my number (its between 1 and 10) >> "))
while guess != mysteryNumber:
    print("Wrong!")
    guess = int(input("Guess my number (its between 1 and 10) >> "))
print("You found my number!")
