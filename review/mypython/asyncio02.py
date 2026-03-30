import asyncio

async def foo(n):
    await asyncio.sleep(n)
    print(f"任务 {n} 完成")
    return n

async def main():
    # 1. 先创建 Task 对象集合
    tasks = {
        asyncio.create_task(foo(1)),
        asyncio.create_task(foo(2)),
        asyncio.create_task(foo(3))
    }

    # 2. 调用 wait，默认会等所有任务完成
    done, pending = await asyncio.wait(tasks)

    print(f"\n已完成的任务数: {len(done)}")
    print(f"未完成的任务数: {len(pending)}") # 这里是 0
    print(done)#集合存三个完成的任务对象
    # 3. 从 done 里获取结果（注意：集合是无序的）
    for task in done:
        print(f"拿到结果: {task.result()}")

asyncio.run(main())