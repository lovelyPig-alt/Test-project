# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import datetime
import requests
import random
import time
import argparse


# end_date = datetime.datetime.strptime("2021-8-20 14:35:00", "%Y-%m-%d %H:%M:%S")  # 结束时间

def logger(txt):
    print("{}:{}".format(datetime.datetime.now(), txt))

def main(openid):

    start_url = "https://h5.amo9.com/h5/2021/july/icecreamapp/start.do?openid={}".format(openid)
    base_post_score_url = "https://h5.amo9.com/h5/2021/july/icecreamapp/end.do?openid={}&id={}&score={}"
    get_rank_url = "https://h5.amo9.com/h5/2021/july/icecreamapp/rank.do?openid={}&page=1&pagesize=100".format(openid)

    flag = True
    while flag:
        # current_data = datetime.datetime.now()
        # if current_data>end_date:
        #     print("break")
        #     flag = False
        #     break
        rank_response = requests.get(get_rank_url).json()
        # print(rank_response)
        self_current_rank = rank_response["self"]["ranking"]
        # self_current_nick = rank_response["self"]["nick"]
        self_currnet_score = rank_response["self"]["score"]
        # logger("当前个人信息:rank:{},nick:{},score:{}".format(self_current_rank,self_current_nick,self_currnet_score))
        logger("当前个人信息:rank:{},score:{}".format(self_current_rank, self_currnet_score))
        first_rank_rank = rank_response["data"][0]["ranking"]
        first_rank_nick = rank_response["data"][0]["nick"]
        first_rank_score = rank_response["data"][0]["score"]
        logger("当前榜单:rank:{},nick:{},score:{}".format(first_rank_rank, first_rank_nick, first_rank_score))

        # 如果当前用户不是榜单 持续刷榜
        if int(self_current_rank)!= first_rank_rank:
            # 提交的分数为第一名的分数 随机加200-400
            post_score = int(first_rank_score) + random.randint(2, 4)
            # game id 由开始游戏时获取 结束时提交分数需要该id
            game_id = requests.get(start_url).json()["id"]
            logger("当前游戏id:{}".format(game_id))
            post_score_url  = base_post_score_url.format(openid, game_id, post_score)
            logger("提交分数:{}".format(post_score))
            logger(post_score_url)
            try:
                time.sleep(1)
                post_score_response = requests.get(post_score_url).text
            except Exception as e:
                logger("异常信息：{}".format(e))
            else:
                logger("当前提交信息:{}".format(post_score_response))
        else:
            logger("当前个人已排第一名")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Testing")
    parser.add_argument("--id", default="", type=str)
    main("00294287744")