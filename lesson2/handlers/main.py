#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2021/1/25 14:37
# @Author :123
# @File : main.PY
# @Software :PyCharm

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

class ExploreHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("explore.html")

class PostHandler(tornado.web.RequestHandler):
    def get(self,post_id):
        self.render("post.html",post_id = post_id)