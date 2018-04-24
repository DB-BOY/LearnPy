# -*- coding: utf-8 -*-
import threading
import time

'多线程'


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()  # 提前加入
print('thread %s ended.' % threading.current_thread().name)

print('===========lock===========')

# 假定这是你的银行存款:
balance = 0

print('线程不安全实例')


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    print("++++++++", threading.current_thread().name, '------', balance)

    balance = balance - n
    print('-----------', threading.current_thread().name, '------', balance)


def run_thread(n):
    for i in range(100):
        change_it(n)


# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


print('')
print('线程安全实例,加锁 lock')

lock = threading.Lock()


def run_thread(n):
    for i in range(1000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
