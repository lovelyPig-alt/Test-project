# coding:utf-8
import easygui as a
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

# 请求流程

'''
    title = "请输入openid"
    msg = "openid"
    openid = a.enterbox(title=title, msg=msg)
'''
# 18718041119
openid = "00237576369"

def getId():
    url = "https://h5.amo9.com/h5/2021/july/icecreamapp/start.do"
    data = {
        "openid": openid
    }
    response = requests.get(url=url, params=data)
    response1 = response.json()
    text = response1["id"]
    return text


gg = getId()


def request():
    # title1 = "请输入分数"
    # msg1 = "请输入分数"
    # score = a.enterbox(title=title1, msg=msg1)

    score = "15490"
    url1 = "https://h5.amo9.com/h5/2021/july/icecreamapp/end.do"
    data1 = {
        "openid": openid,
        "id": gg,
        "score": score
    }
    response = requests.get(url=url1, params=data1)
    tltie2 = "结果"
    msg2 = response.text
    a.msgbox(title=tltie2, msg=msg2)

# # Blockingscheduler
scheduler = BlockingScheduler()
scheduler.add_job(request, 'cron', hour=23, minute=59, second=1)
scheduler.start()
