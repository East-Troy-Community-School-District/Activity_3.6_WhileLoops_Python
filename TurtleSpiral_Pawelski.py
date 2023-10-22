'''
Turtle Spiral
Pawelski
10/22/2023
Introduction to Computer Science

Instructions:
Run the program and see what it draws. Next, let's discuss a few
questions...
1. What does the program draw?
2. How does the loop improve this program? (HINT: Why would you
   not want to write this program without loops?)
3. How many times does the loop repeat?
4. What is the loop control variable?
5. How would you modify the program so that the spiral is tighter?
   Less tight? Test your modifications to see if you are correct!
6. How could you run the program one step at a time to see how
   it executes?
'''


import turtle

t = turtle.Turtle()
t.pensize(6)

distance = 5
while distance < 100:
    t.forward(distance)
    t.left(15)
    distance = distance + 1

turtle.mainloop()