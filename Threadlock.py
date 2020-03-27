import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


for i in range(10):  
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # if balance != 0:
    #     print(balance) 
    # else:
    #     pass
    print(balance)
    balance = 0


    # 因为Python的线程虽然是真正的线程，
    # 但解释器执行代码时，有一个GIL锁：
    # Global Interpreter Lock，任何
    # Python线程执行前，必须先获得GIL锁，
    # 然后，每执行100条字节码，解释器就自
    # 动释放GIL锁，让别的线程有机会执行。
    # 这个GIL全局锁实际上把所有线程的执行代
    # 码都给上了锁，所以，多线程在Python中
    # 只能交替执行，即使100个线程跑在100核
    # CPU上，也只能用到1个核。