try:
    file=open('eeee.txt','r+')
except Exception as e:
    print(e)
    response = input('do you want to create a new file:')
    if response=='y':
        file=open('eeee.txt','w')
    else:
        pass
else:
    file.write('ssss')
    file.close()
"""
[Errno 2] No such file or directory: 'eeee.txt'
do you want to create a new file:y

ssss  #eeee.txt中会写入'ssss'
"""