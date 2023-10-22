'''
Bottles of Pop
Pawelski
10/22/2023
Introduction to Computer Science

Instructions:
Trace the program and predict what it will display.
Then run the program to check your work. Finally, be prepared
to discuss the following questions...
1. Why was the phrase "No more bottles of pop on the wall!"
   printed only one time?
2. How do you indicate that lines are inside a loop? Outside
   a loop?
3. How could you modify the program so that it starts counting
   at 10,000? What about 100,000? Test your theory by chaning
   the code and seeing if you are right!
4. Why is it better to use loops instead of repeating the same
   line multiple times?
'''

bottles = 1000
while bottles > 0:
    print(str(bottles) + " bottle(s) of pop on the wall.")
    bottles = bottles - 1
print("No more bottles of pop on the wall!")