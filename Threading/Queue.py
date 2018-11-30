import threading
import time
from queue  import Queue

def job(L,q):
    for i in range(len(L)):
        L[i] = L[i]**2
    q.put(L)

def multithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[4,4,4],[5,5,5],[6,6,6]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    result = []
    for i in range(4):
        result.append(q.get())
    print(result)

multithreading()