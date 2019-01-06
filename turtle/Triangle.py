import turtle
import time

#Length of triangle
a = 60

for i in range(10):
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    a = a + i*4

time.sleep(10)

