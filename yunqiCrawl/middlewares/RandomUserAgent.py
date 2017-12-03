#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-3 16:53:49
# @File : RandomUserAgent.py
# @Software : IntelliJ IDEA
import random
'''
这个类主要用于产生随机UserAgent
'''

class RandomUserAgent(object):

    def __init__(self,agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))#返回的是本类的实例cls ==RandomUserAgent

    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))