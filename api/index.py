Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@yyds-space 
Eurkon
/
weibo-top-api
Public
Fork your own copy of Eurkon/weibo-top-api
Code
Issues
Pull requests
Actions
Projects
Security
Insights
Beta Try the new code view
weibo-top-api/api/index.py /
@Eurkon
Eurkon refactor: 重构爬取微博热搜
Latest commit 94333b1 on Nov 10, 2021
 History
 1 contributor
71 lines (58 sloc)  1.72 KB

# -*- coding: utf-8 -*-
# @Author    : Eurkon
# @Date      : 2021/6/5 10:16

import json
import time
import requests
from http.server import BaseHTTPRequestHandler


def get_data():
    """微博热搜
    Args:
        params (dict): {}
    Returns:
        json: {title: 标题, url: 地址, num: 热度数值, hot: 热搜等级}
    """

    data = []
    response = requests.get("https://weibo.com/ajax/side/hotSearch")
    data_json = response.json()['data']['realtime']
    jyzy = {
        '电影': '影',
        '剧集': '剧',
        '综艺': '综',
        '音乐': '音'
    }

    for data_item in data_json:
        hot = ''
        # 如果是广告，则不添加
        if 'is_ad' in data_item:
            continue
        if 'flag_desc' in data_item:
            hot = jyzy.get(data_item['flag_desc'])
        if 'is_boom' in data_item:
            hot = '爆'
        if 'is_hot' in data_item:
            hot = '热'
        if 'is_fei' in data_item:
            hot = '沸'
        if 'is_new' in data_item:
            hot = '新'

        dic = {
            'title': data_item['note'],
            'url': 'https://s.weibo.com/weibo?q=%23' + data_item['word'] + '%23',
            'num': data_item['num'],
            'hot': hot
        }
        data.append(dic)

    return data


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_data()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return


if __name__ == '__main__':
    print(get_data())
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
weibo-top-api/index.py at main · Eurkon/weibo-top-api
