#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2021/1/25 14:37
# @Author :123
# @File : main.PY
# @Software :PyCharm

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        imgs = []
        for i in range(1,5):
            imgs.append("imgs/{}.jpg".format(i))
        self.render("index.html",imgs=imgs)

class ExploreHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("explore.html")

class PostHandler(tornado.web.RequestHandler):
    def get(self,post_id):
        self.render("post.html",post_id = post_id)