# -*aiohttp[基于asyncio实现的HTTP框架 | 示例参考https://www.cntofu.com/book/127/aiohttp%E6%96%87%E6%A1%A3/Introduce.md]
import asyncio

import aiohttp
import async_timeout
from aiohttp import web


# 客户端例子
async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as r:
            return await r.text()


async def main():
    async with aiohttp.ClientSession() as s:
        html = await  fetch(s, 'http://wanandroid.com')
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# 服务端例子
async def handle(request):
    name = request.match_info.get('name', 'ashe')
    text = 'hello, ' + name
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app)
