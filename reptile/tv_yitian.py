# coding=utf-8
from urllib.error import HTTPError

from pyquery import PyQuery

# 遍历地址
for i in range(27, 50):
    url = 'http://xyttlj.shouyouyou.com/play/1-' + str(i) + '.html'
    # 倚天屠龙记
    try:
        movie_response = PyQuery(url)
        div_address = movie_response('.am-u-sm-12').siblings()
        a_address = div_address.children('p').children('a')
        print('第' + str(i) + '集 >>>>> ' + a_address.attr('href'))
    except HTTPError:
        print('Not found. >>>>> ' + url)
