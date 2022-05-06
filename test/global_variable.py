#!/usr/bin/env python

# 测试定义全局变量，并修改变量内容

def setup():
    global temp
    temp = 10086
    print('........ setup ........', temp)
    temp += 1


def loop():
    while True:
        pass


def destroy():
    print('........ destroy ........', temp)


if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
