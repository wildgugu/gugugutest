import threading
import queue
import time


def worker(q):
    name=threading.current_thread().name
    while not q.empty():
        item = q.get()
        print(f"{name}处理项目: {item}")
        time.sleep(1)
        q.task_done()

# 创建一个队列并填充数据
q = queue.Queue()
for i in range(10):
    q.put(i)

# 创建线程实例
thread1 = threading.Thread(target=worker, args=(q,))
thread2 = threading.Thread(target=worker, args=(q,))
# 启动线程
thread1.start()
thread2.start()
# 等待队列中的所有项目被处理完毕
q.join()
print("所有项目处理完毕")