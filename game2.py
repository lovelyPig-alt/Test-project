# coding=utf-8

import datetime
import requests
import random
import time
import argparse
import threading
from queue import  Queue

def logger(txt):
    print("{}:{}".format(datetime.datetime.now(),txt))

def generate_openid():
    print("generate start")
    openid_queue = Queue()
    base_start_openid = 200000000

    generate_number = 50000000
    # generate_number = 1000
    for i in range(generate_number):
        base_start_openid += 1
        openid = "00" + str(base_start_openid)
        openid_queue.put(openid)
    print("generate over")

    return openid_queue

def get_id(openid_queue):
    base_get_rank_url = "https://h5.amo9.com/h5/2021/july/icecreamapp/rank.do?openid={}&page=1&pagesize=100"

    nicks = ["ITBOB", "暂无名", "程龙", "彭斯博", "11c", "ThunderLei", "抓周游"]

    while not openid_queue.empty():
        openid = openid_queue.get()
        get_rank_url = base_get_rank_url.format(openid)
        rank_response = requests.get(get_rank_url).json()

        try:
            self_current_nick = rank_response["self"]["nick"]
            if self_current_nick in nicks:
                print("获取到nick:{},id:{}".format(self_current_nick,openid))
                with open("openid.txt","a+") as f:
                    f.write("{} {}\n".format(self_current_nick,openid))
        except Exception as e:
            logger("{} {}".format(openid,e))
def main():
    thread_number = 10
    thread_pool = []
    openid_queue= generate_openid()
    for i in range(thread_number):
        thread = threading.Thread(target=get_id,args=(openid_queue,))
        thread_pool.append(thread)
    for one in thread_pool:
        one.start()

    for one in thread_pool:
        one.join()

if __name__ == '__main__':

    main()