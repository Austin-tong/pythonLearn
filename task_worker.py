import time, sys, queue 
from multiprocessing.managers import BaseManager

#创建类似的manager
class QueueManager(BaseManager):
    pass

#获取用只注册名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接服务器
sever_addr = '127.0.0.1'
print('Connect to server %s...' %sever_addr)
#端口验证码
m = QueueManager(address=(sever_addr, 5000), authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' %(n,n))
        r = '%d * %d = %d' %(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

print('worker exit.')