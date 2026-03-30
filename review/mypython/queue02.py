import queue

# 创建一个队列
q = queue.Queue()
lifo=queue.LifoQueue()
poq=queue.PriorityQueue()
# 向队列中添加元素
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出: 1
print(q.get())  # 输出: 2
print(q.get())  # 输出: 3


# 向队列中添加元素
lifo.put(1)
lifo.put(2)
lifo.put(3)

# 从队列中获取元素
print(lifo.get())  # 输出: 3
print(lifo.get())  # 输出: 2
print(lifo.get())  # 输出: 1

# 向队列中添加元素，元素为元组 (优先级, 数据)
poq.put((3, 'Low priority'))
poq.put((1, 'High priority'))
poq.put((2, 'Medium priority'))

# 从队列中获取元素
print(poq.get())  # 输出: (1, 'High priority')
print(poq.get())  # 输出: (2, 'Medium priority')
print(poq.get())  # 输出: (3, 'Low priority')