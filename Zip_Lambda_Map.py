"""zip"""

a = [1,2,3]
b = [4,5,6]

print(list(zip(a,b)))

for i,j in zip(a,b):
    print(i/2,j*2)

c = [7,8,9]
print(list(zip(a,b,c)))

"""lambda"""
func = lambda x ,y: x+y
print(func(2,3))

"""map"""
z = map(func,[1,2,3],[2,3,4])
print(list(z))
