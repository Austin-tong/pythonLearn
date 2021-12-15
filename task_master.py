import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接受结果的队列
result_queue = queue.Queue()

#从Basemanager集成的queuemanager
class QueueManager(BaseManager):
    pass

def f1():
    return task_queue

def f2():
    return result_queue

if __name__ == '__main__':
    #queue注册到网络上
    QueueManager.register('get_task_queue', callable=f1)
    QueueManager.register('get_result_queue', callable=f2)
    #绑定端口5000，设置验证码'abc'
    manager = QueueManager(address=('localhost', 5000), authkey=b'abc')
    #启动queue
    manager.start()
    #获得通过网络访问的queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    #放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' %n)
        task.put(n)
    #从result读取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=150)
        print('Result: %s' %r)
    #关闭
    manager.shutdown()
    print('master exit')
