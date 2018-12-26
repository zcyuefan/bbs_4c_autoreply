# bbs_4c_autoreply
第四城论坛灌水机器人

## 安装与使用
1.设置好发帖内容和帖子ID

    message = random.choice([
        "顶帖",
        "顶顶更健康",
        "[img]75[img]",
        "{:16_804:}"
    ])
    post_id = ""  # 帖子ID

2.将以"; "分割的cookies内容放在cookies.txt中

3.通过windows任务计划程序或者Linux crontab设置定时任务即可自动水贴