#!/usr/bin/env python
import time

import RPi.GPIO as GPIO

# 感应开关控制 RGB 小灯

# 实现: while true监听输入的针脚, 如果有输入, 则亮绿灯

SWITCH_IN = 12

R = 16
G = 20

# 如果灯已经关了, 就没必要再关一次了
LOW_CACHE = {"needChange": True}


def init():
    # 启用GPIO.BCM编号(不同版本的树莓派不一样); 还有一种GPIO.BOARD(不用看接口图,数引脚1~40就可以接线)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SWITCH_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # init rgb led
    GPIO.setup(G, GPIO.OUT)


def pinsOutput(signal):
    if signal:
        GPIO.output(G, GPIO.HIGH)
        LOW_CACHE['needChange'] = False
    else:
        if LOW_CACHE['needChange'] == False:
            print('touch set low level...')
            LOW_CACHE['needChange'] = True
            GPIO.output(G, GPIO.LOW)


# 循环相关操作
def loop():
    # GPIO.add_event_detect(SWITCH_IN, GPIO.BOTH, callback = pinsOutput, bouncetime = 200)

    while True:
        time.sleep(0.5)
        if GPIO.input(SWITCH_IN):
            time.sleep(0.5)
            if GPIO.input(SWITCH_IN):
                print('touched, light on')
                pinsOutput(GPIO.HIGH)
        else:
            pinsOutput(GPIO.LOW)


# 销毁操作
def destroy():
    GPIO.cleanup()


# Main程序
if __name__ == "__main__":
    try:
        init()
        loop()
    except KeyboardInterrupt:
        destroy()
