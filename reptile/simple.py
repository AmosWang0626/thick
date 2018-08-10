# coding=utf-8

# Two download methods.
# 1.urllib2
# 2.requests

import json
from urllib import request

# 第一种方式,简单请求
# 直接请求
firstResponse = request.urlopen('https://www.baidu.com')
# 获取状态码以及输出
print(firstResponse.getcode())
# 读取内容
print(firstResponse.read())

# 第二种方式,设置数据请求
print('================================== 华丽丽的分隔符 ==================================')
# 添加数据
secondHeader = {
    'User-Agent': 'Chrome/68.0.3440.84',
    'token': 'HLF465FDA13G98',
    'Content-Type': 'application/json'
}
secondData = {
    'name': 'amos',
    'content': 'hello'
}
tempData = bytes(json.dumps(secondData), 'utf-8')

# GET 请求
secondRequest = request.Request('http://www.microcn.top:8080/hi0?name=amos&content=hello',
                                headers=secondHeader)
# POST 请求
secondRequest = request.Request('http://www.microcn.top:8080/person',
                                headers=secondHeader, data=tempData)
secondResponse = request.urlopen(secondRequest)
print(secondResponse.getcode())
print(secondResponse.read())
