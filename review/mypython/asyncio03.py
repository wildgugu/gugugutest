import asyncio

async def fetch_from_server(server_id):
    # 模拟不同服务器的响应速度
    delay = server_id * 0.5
    await asyncio.sleep(delay)
    return f"来自服务器 {server_id} 的数据"

async def main():
    tasks = {
        asyncio.create_task(fetch_from_server(1)),
        asyncio.create_task(fetch_from_server(2)),
        asyncio.create_task(fetch_from_server(3))
    }

    # 1. 等待，只要有第一个完成就立刻返回
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # 2. 处理最快的那个结果
    fastest_task = done.pop()
    print(f"最快结果: {fastest_task.result()}")

    # 3. 【关键】取消剩下还在跑的任务（节省资源）
    for task in pending:
        task.cancel()
        print(f"已取消任务: {task}")

asyncio.run(main())