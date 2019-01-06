import turtle
import time

LENGHT = 120

t = turtle.Turtle()
t.fillcolor('blue')
t.begin_fill()

t.speed(1)    #调整画笔速度   1-10
time.sleep(1)
t.up()        #画笔抬起不绘制图形
t.goto(10,10)
t.down()      #画笔落下开始绘制图形

t.pensize(20) #画笔宽度
t.pencolor('red')

for i in range(4):
    t.forward(LENGHT)
    t.left(90)
t.end_fill()

t.begin_fill()
time.sleep(1)
t.fillcolor('red')
t.pensize(10) #画笔宽度
t.pencolor(0., 0., 1)
t.up()
t.goto(-50,-50)
t.down()
t.circle(radius=50, extent=270)
t.end_fill()
time.sleep(3)

"""
(1)运动命令:

forward(d)  向前移动距离d代表距离

backward(d) 向后移动距离d代表距离

right(degree)   向右转动多少度

left(degree)    向左转动多少度

goto(x,y)   将画笔移动到坐标为(x,y)的位置

stamp()     绘制当前图形

speed(speed)    画笔绘制的速度范围[0,10]整数

(2)画笔控制命令:

down() 画笔落下，移动时绘制图形

up()    画笔抬起，移动时不绘制图形

setheading(degree)  海龟朝向，degree代表角度

reset() 恢复所有设置

pensize(width)  画笔的宽度

pencolor(colorstring)   画笔的颜色

fillcolor(colorstring)  绘制图形的填充颜色

fill(Ture)
 
fill(False)

circle(radius, extent)  绘制一个圆形，其中radius为半径，extent为度数，例如若extent为180，则画一个半圆；如要画一个圆形，可不必写第二个参数
"""