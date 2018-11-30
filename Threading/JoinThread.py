"""
    join 意思为 等待该线程结束后 主程序继续运行

"""
import threading
import time


def thread_job():
    print('T1 start \n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finished\n')

def thread2_job():
    print('T2 start \n')
    print('T2 finished\n')


def main():
    #添加两个线程
    added_thread = threading.Thread(target=thread_job,name='T1')
    thread2 = threading.Thread(target=thread2_job,name='T2 ')

    #开始两个线程
    added_thread.start()
    thread2.start()

    #添加join
    thread2.join()


if __name__ == '__main__':
    main()