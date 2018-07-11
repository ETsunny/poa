import logging

# 配置logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


def setup_routes(app):
    app.router.add_route('GET', '/', index)


def init():
    app = web.Application()
    setup_routes(app)
    web.run_app(app=app, port=9000)


if __name__ == '__main__':
    init()
