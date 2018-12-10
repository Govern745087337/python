import multiprocessing as mp

#设置共享内存  'd'为type
value = mp.Value('d',0)
#只能用一维
array = mp.Array('i',[1,3,4])

