import asyncio

count = 0

async def add_one():
    global count
    # 1. 读取当前值 (假设读到 0)
    tmp = count
    # 2. 这里有个 await，协程切换出去了！
    await asyncio.sleep(1)
    # 3. 切回来，把 tmp+1 (1) 写回去
    count = tmp + 1

async def main():
    global count
    count = 0
    # 并发运行两个加 1 的任务
    await asyncio.gather(add_one(), add_one())
    print(f"期望结果: 2, 实际结果: {count}") # 实际结果可能是 1！

asyncio.run(main())