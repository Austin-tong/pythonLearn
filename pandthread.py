from multiprocessing import Process, Pool, Queue
import os, time, random, subprocess, threading, multiprocessing

"""
def run_proc(name):
    print('Run child process %s (%s)...' %(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s' %os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
"""
"""
def long_time_task(name):
    print('Run task %s (%s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name,(end-start)))

if __name__ == '__main__':
    print('Parent process %s' %os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
"""

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('exit code:', p.returncode)
"""
def write(q):
    print('Process to write: %s' %os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' %value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' %os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' %value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
"""

"""def loop():
    print('thread %s is running...' %threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)

print('thread %s is running...' %threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' %threading.current_thread().name)
"""

"""balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(balance, (end-start))
"""

def loop():
    x = 0
    while True:
        x = x^1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()


