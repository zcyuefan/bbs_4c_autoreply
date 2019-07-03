# bbs_4c_autoreply
第四城论坛灌水机器人

## 使用设置
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

通过windows任务计划程序或者Linux crontab设置定时任务即可自动水贴

# 命令
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u zcyuefan -p yuefan -c 5
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u yanghao -p yuefan -c 5
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u zcyuefan -p 默默熙 -c 5
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u zcyuefan -p ying姐 -c 5
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u zcyuefan -p Noriyasu -c 5
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u zcyuefan -p 岁岁平安 -c 5
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u zcyuefan -p 惠蕙 -c 5
F:\05-python-projects\bbs_4c_autoreply\venv\Scripts\python.exe F:/05-python-projects/bbs_4c_autoreply/run.py -u zcyuefan -p 小鱼鱼哟 -c 5