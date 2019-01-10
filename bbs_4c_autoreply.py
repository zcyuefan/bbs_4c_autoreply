#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    bbs_4c_autoreply
    -----------------------------
    实现第四城论坛自动灌水，通过设置自动任务（如linux的crontab）自动评论帖子
    :copyright: (c) 2018 by zcyuefan.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

import requests
import random
import time
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    filename='post.log',
                    filemode='a')


class User:
    """
    登录账户类
    """
    def __init__(self, name, sleep_seconds_from, sleep_seconds_to, raw_cookies):
        self.name = name
        self.cookies = self.parse_cookies(raw_cookies)
        self.sleep_seconds_from = sleep_seconds_from
        self.sleep_seconds_to = sleep_seconds_to

    @staticmethod
    def parse_cookies(raw_cookies):
        if isinstance(raw_cookies, str):
            return dict([i.split("=", 1) for i in raw_cookies.strip().split("; ")])
        else:
            return raw_cookies

    def reply(self, post, message):
        url = "http://www.4c.cn/post.php"
        params = dict(action="reply", fid=3555, tid=post.tid, extra="", replysubmit="yes", infloat="yes",
                      handlekey="fastpost")
        data = dict(formhash="4f01ab25", subject="", usesig=0, message=message, replysubmit="replysubmit", toend=1)
        headers = {
            "Host": "www.4c.cn",
            "Connection": "keep-alive",
            "Content-Length": "94",
            "Cache-Control": "max-age=0",
            "Origin": "http://www.4c.cn",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "DNT": "1",
            "Referer": "http://www.4c.cn/thread-%s-1-1.html" % post.tid,
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
        }
        req = requests.post(url=url, params=params, data=data, headers=headers, cookies=self.cookies)
        if req.status_code == 200 and req.text.find("您的回复已经发布") > 0:
            logging.info("{}回复{}的帖子{}成功".format(self.name, post.floor_owner, post.subject))
        else:
            logging.info("{}回复{}的帖子{}失败".format(self.name, post.floor_owner, post.subject))
            logging.error("req.text")

    def reply_many(self, post, *more_messages):
        for message in more_messages:
            self.reply(post, message)
            sleep_time = random.randint(self.sleep_seconds_from, self.sleep_seconds_to)
            logging.info("{}休息{}秒".format(self.name, sleep_time))
            time.sleep(sleep_time)


class Post:
    """
    贴子类
    """

    def __init__(self, tid, floor_owner, subject):
        self.tid = tid
        self.floor_owner = floor_owner
        self.subject = subject


if __name__ == "__main__":
    messages = [
        "顶顶更健康",
        "[img]75[img]",
        "{:16_804:}",
        "[img]72[img][img]80[img]"
    ]
    random_sleep_range = [30, 180]
    # 实例化用户
    your_user = User(name='your_user',
                     sleep_seconds_from=random_sleep_range[0],
                     sleep_seconds_to=random_sleep_range[1],
                     raw_cookies="""
                    用'; '分割的cookies
                    """)

    # 实例化帖子
    your_post = Post('1111111', '小明', 'xxxx……')
    # 单条回复
    your_user.reply(your_post, messages[0])
    # 多条回复
    your_user.reply_many(your_post, *random.sample(messages, 3))
