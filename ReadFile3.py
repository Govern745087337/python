file= open('my file.txt','r')
content=file.read()
print(content)

"""
This is my first test.
This is the second line.
This the third line.
This is appended file.    
"""

file= open('my file.txt','r')
content=file.readline()  # 读取第一行
print(content)
"""
This is my first test.
"""
second_read_time=file.readline()  # 读取第二行
print(second_read_time)
"""
This is the second line.
"""

#读取所有行
file= open('my file.txt','r')
content=file.readlines() # python_list 形式
print(content)
