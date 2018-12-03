"""
正则表达式
"""
#coding:utf-8
import re  #正则表达式模块

#简单python匹配
pattern1 = 'cat'
pattern2 = 'dog'
string = 'cat eats the mouse'
print(pattern1 in string)
print(pattern2 in string)

#正则表达式找匹配
pattern1 = 'cat'
pattern2 = 'dog'
string = 'cat eats the mouse'
print(re.search(pattern1,string))
print(re.search(pattern2,string))

#正则表达式多种可能匹配
ptn = r"c[ao]t"
string = 'cat eats the mouse'
print(re.search(ptn,string))

#匹配更多可能
print(re.search(r"c[A-Z]t",string))   #匹配大写
print(re.search(r"c[a-z]t",string))   #匹配小写
print(re.search(r"c[0-9]t",string))   #匹配数字
print(re.search(r"c[0-9a-z]t",string))   #匹配数字和小写

#特殊种类匹配
print(re.search(r"c\dt",string))     # \d表示匹配数字
print(re.search(r"c\Dt",string))     # \D表示不是数字的形式

print(re.search(r"c\st",string))     # \s表示空白符     \t\n\f\r
print(re.search(r"c\St",string))     # \S表示非空白符

print(re.search(r"c\wt",string))     # \w表示匹配a-z A-Z 0-9 _
print(re.search(r"c\Wt",string))     # \W表示反面

print(re.search(r"\bcat\b",string))  # 表示匹配前后空格的字符串
print(re.search(r"\B cat \B",string))  # 表示不管是否有空白格都可以匹配到    **

print(re.search(r"run\\","hello run\ "))     # \\表示匹配反斜杠  前边加反斜杠表示匹配特殊字符
print(re.search(r"c.t",string))     # .表示匹配任意

print(re.search(r"^cat",string))     # ^表示匹配句首
print(re.search(r"mouse$",string))     # $表示匹配句尾

print(re.search(r"Mon(day)?","Monday"))   #匹配两种
print(re.search(r"Mon(day)?","Mon"))

string1 = """
dogs run to cat.
I run to dog.
"""
print(re.search(r"\.$",string1,flags=re.M))    #加入标志位可以逐行判断

print(re.search(r"ab*","a"))            #出现0次或多次
print(re.search(r"ab*","abbbbbb"))

print(re.search(r"ab+","a"))            #出现1次或多次
print(re.search(r"ab+","abbbbbb"))

print(re.search(r"ab{2,10}","a"))      #可选次数  2次到10次
print(re.search(r"ab{2,15}","abbbbbb"))

#\d+表示匹配数字出现一次或多次 .+表示匹配所有
match = re.search(r"(\d+),Date:(.+)","ID:021523,Date:Feb/12/2017...")
print(match.group())
print(match.group(1))               #1表示第几个括号里边的东西
print(match.group(2))

match = re.search(r"(?P<id>\d+),Date:(?P<date>.+)","ID:021523,Date:Feb/12/2017...")
print(match.group('id'))               #给组加一个名字
print(match.group('date'))

#找到所有
print(re.findall(r"r[au]n","ran run ran"))\

#替换
print(re.sub(r"r[au]ns","catchs","dogs runs to cat"))

#分裂
print(re.split(r'[,;\.]',"a,b,c,d;e"))