import asyncio
from asyncore import loop

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:  # async with 用于异步上下文管理器
        return await response.text()


async def main():
    urls = [
        "https://www.python.org",
        "https://www.baidu.com",
        "https://www.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        # 列表推导式创建协程对象列表
        tasks = [fetch(session, url) for url in urls]
        # 并发执行
        results = await asyncio.gather(*tasks)

        for url, html in zip(urls, results):
            print(f"{url} 内容长度: {len(html)}")


asyncio.run(main())
