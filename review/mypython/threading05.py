import random
import threading
from threading import Condition

queue = []
cond = Condition()
MAX_ITEMS = 5

def producer():

    """
    生产者函数，用于向队列中生成随机数项。
    当队列未满时，生成一个随机数并添加到队列中。
    当队列满时，生产者会等待，直到队列中有空间。
    """
    for _ in range(10):  # 循环10次，生成10个随机数项
        with cond:  # 使用条件变量进行同步控制
            # 当队列已满时，生产者等待
            while len(queue) >= MAX_ITEMS:
                cond.wait()
            # 生成1到100之间的随机数
            item = random.randint(1, 100)
            # 将生成的随机数添加到队列中
            queue.append(item)
            # 打印生产信息
            print(f"Produced {item}")
            # 通知其他可能task
            cond.notify()

def consumer():
    # 循环10次，模拟消费者消费10个商品
    for _ in range(10):
        # 使用with语句获取条件变量cond的锁
        with cond:
            # 当队列为空时，消费者等待
            while not queue:
                cond.wait()
            # 从队列头部取出一个商品
            item = queue.pop(0)
            # 打印消费的商品信息
            print(f"Consumed {item}")
            # 通知其他等待的task
            cond.notify()

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()