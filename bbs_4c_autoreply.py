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
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    filename='post.log',
                    filemode='a')


def parse_cookies(raw_cookies):
    if isinstance(raw_cookies, str):
        return dict([i.split("=", 1) for i in raw_cookies.split("; ")])
    else:
        return raw_cookies


if __name__ == "__main__":
    # 最新的cookie和消息内容设置
    message = random.choice([
        "顶帖",
        "顶顶更健康",
        "[img]75[img]",
        "{:16_804:}"
    ])
    post_id = ""  # 帖子ID
    # 请求基本设置
    host = "www.4c.cn"
    url = "http://www.4c.cn/post.php"
    params = dict(action="reply", fid=3555, tid=post_id, extra="", replysubmit="yes", infloat="yes",
                  handlekey="fastpost")
    data = dict(formhash="4f01ab25", subject="", usesig=0, message=message, replysubmit="replysubmit",toend=1)
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
        "Referer": "http://www.4c.cn/thread-%s-1-1.html" % post_id,
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
    }
    # 设置随机延时
    is_delay = False
    delay_seconds = random.randint(15, 180)

    with open('cookies.txt') as f:
        cookies = parse_cookies(f.readline())

    if is_delay:
        import time
        time.sleep(delay_seconds)

    req = requests.post(url=url, params=params, data=data, headers=headers, cookies=cookies)
    if req.status_code == 200 and req.text.find("您的回复已经发布"):
        logging.info("Post Successful")
    else:
        logging.error("Post Failed")
        logging.error("req.text")
