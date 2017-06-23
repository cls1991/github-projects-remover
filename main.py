# coding: utf8

import os
# 切换工作目录到项目根目录
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

from core.github import GithubSample


if __name__ == '__main__':
    gs = GithubSample('8709c9b9d01ec8e7388378c3992eff61aa7df813')
    # pretty_print(gs.query_api_info())
    # pretty_print(gs.query_user_info('cls1991'))
    # pretty_print(gs.query_user_repos('cls1991'))
    # print(gs.star_repo('torvalds', 'linux'))
    """
       star all forked repos, then remove all, for personal use!
    """
    user_repos = gs.query_user_repos('cls1991', page=1, per_page=50)
    # pretty_print(user_repos)
    for repo in user_repos:
        if repo['fork']:
            repo_info = gs.query_repo_info('cls1991', repo['name'])
            if 'source' not in repo_info:
                continue
            status_code = gs.star_repo(repo_info['source']['owner']['login'], repo['name'])
            print(status_code)
            if status_code == 204:
                gs.remove_repo('cls1991', repo['name'])
