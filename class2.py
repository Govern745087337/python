#coding:utf-8
class Calculator:
    def __init__(self,name="Good cac",price=1,height=2,width=3,weight=4):
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.weight = weight
        self.add(weight,height)   #定义时直接执行

    def add(self,x,y):
        print(x+y)

    def sub(self,x,y):
        print(x-y)

c = Calculator(name='bad cac',price=18,weight=1,height=2,width=3)
print(c.name)

b = Calculator()
print(b.name)