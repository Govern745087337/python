import turtle
import time
import random

init_pos_x = -300
init_pos_y = -300
circle_num = 25

#初始化turtle对象
t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(init_pos_x, init_pos_y)
t.down()

def DrawCircle(pos_x,pos_y,radius):
    t.up()
    t.goto(pos_x, pos_y)
    t.down()
    t.color(random.random(),random.random(),random.random())
    t.begin_fill()
    t.circle(radius=radius, extent=360)
    t.end_fill()


def DrawHeart():
    t.up()
    t.goto(-50, -50)
    t.down()

    def curvemove():
        for i in range(200):
            t.right(1)
            t.forward(1)

    t.color('red', 'pink')
    t.begin_fill()
    t.left(140)
    t.forward(111.65)
    curvemove()
    t.left(120)
    curvemove()
    t.forward(111.65)
    t.end_fill()


def main():
    for i in range(circle_num):
        DrawCircle(init_pos_x,init_pos_y+i*circle_num,60)
    for i in range(circle_num):
        DrawCircle(i*circle_num+init_pos_x,circle_num**2+init_pos_y,60)
    for i in range(circle_num):
        DrawCircle(circle_num**2+init_pos_x,circle_num**2-i*circle_num+init_pos_y,60)
    for i in range(circle_num):
        DrawCircle(circle_num**2-i*circle_num+init_pos_x,init_pos_y,60)
    DrawHeart()
main()
time.sleep(3)
