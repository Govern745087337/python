"""
自动分配多核运算
"""
import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool()
    # pool = mp.Pool(processes=3)  #只用三个核
    res = pool.map(job,range(10))
    print(res)

if __name__ == '__main__':
    multicore()
