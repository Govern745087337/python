
import multiprocessing as mp
import threading as td

def thread_job(a,b):
    print(a+b)

# tl = td.Thread(target=thread_job,args=(1,2))
# tl.start()

##  必须在此框架下应用 否则会报错
if __name__ == '__main__':
    p1 = mp.Process(target=thread_job,args=(1,2))
    p1.start()