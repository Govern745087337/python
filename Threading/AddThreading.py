import threading

def thread_job():
    print("This is a added threading,number is %s",threading.current_thread())

def main():
    #添加一个线程
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    #算一下有多少个激活的线程
    print(threading.active_count())
    #看一下有哪几个激活的线程
    print(threading.enumerate())
    #看现在正在运行的是哪个线程
    print(threading.current_thread())

if __name__ == '__main__':
    main()