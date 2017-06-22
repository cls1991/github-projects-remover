# coding: utf8

import os
# 切换工作目录到项目根目录
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

from core.github import GithubSample, pretty_print


if __name__ == '__main__':
    gs = GithubSample('207ddd9b6819c01019c43d09c65eebff88cee2f8')
    # pretty_print(gs.query_api_info())
    # pretty_print(gs.query_user_info('cls1991'))
    pretty_print(gs.query_user_repos('cls1991'))
