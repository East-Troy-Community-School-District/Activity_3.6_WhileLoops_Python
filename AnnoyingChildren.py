'''
Annoying Children
Pawelski
10/22/2023
Introduction to Computer Science

Instructions:
Before you run the program, trace the code and predict what it
will do. Then, run the code to check your prediction. Finally,
be prepared to discuss the following questions...
1. How many times will the loop run?
2. This is an infinite loop, but not an indefinite loop? What
   is the difference between the two?
3. What do you need to do so that the program only repeats the
   phrase 1,000 times?
4. How would you modify the program so that it only prints
   the phrase 1,094 times (one time for each minute it takes
   to get from East Troy to Disney World).
5. What do you think the the following code does in this program?
   colorama.Fore.MAGENTA
'''

import colorama

time = 1
while time <= 1000:
    print(colorama.Fore.MAGENTA + "Are we there yet?")