#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2021/1/25 10:24
# @Author :123
# @File : app.PY
# @Software :PyCharm

import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define,options
from handlers import main

define("port",default="8080",help="Listening port",type=int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            ("/",main.IndexHandler),
            ("/explore",main.ExploreHandler),
            ('/post/(?P<post_id>[0-9]+)', main.PostHandler),
        ]

        settings = dict(
            debug = True,
            template_path = "template",
            static_path = "static",
            static_url_prefix = "/tupian/"   #一定要加斜杠,需要效果静态文件夹的名称使用
             #这样访问的时候实现从tupian这个路径开始访问图片  如：src="/tupian/imgs/1.jpg"
        )
        super().__init__(handlers,**settings)

application = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print("Server start on port {} ".format(options.port))
    tornado.ioloop.IOLoop.current().start()