#coding:utf-8
class Calculator:
    name = 'Good Calculator'
    price = 18
    def add(self,x,y):
        print(x+y)
    def sub(self,x,y):
        print(x-y)

cal = Calculator() #外部定义个体  个体属于类
print(cal.name)
print(cal.price)
cal.add(2,11)