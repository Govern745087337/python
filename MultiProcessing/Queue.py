import multiprocessing as mp

def thread_job(q,a,b):
    #queue
    c = a+b
    q.put(c)

##  必须在此框架下应用 否则会报错
if __name__ == '__main__':
    #需要创建一个q值
    q = mp.Queue()

    p1 = mp.Process(target=thread_job,args=(q,1,2))
    p2 = mp.Process(target=thread_job, args=(q, 3, 4))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    res1 = q.get()
    res2 = q.get()

    print(res1)
    print(res2)