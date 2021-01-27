#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2021/1/25 10:50
# @Author :123
# @File : hello.PY
# @Software :PyCharm

import tornado.ioloop
import tornado.web

class MainHandle(tornado.web.RequestHandler):
    def get(self):
        self.write("hello,world")

application = tornado.web.Application([
    (r"/",MainHandle),
]
)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()