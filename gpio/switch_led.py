#!/usr/bin/env python
import time

import RPi.GPIO as GPIO

# 触摸开关控制 RGB 小灯

# 实现: 初始化为高电平输出, 然后通过改变占空比, 控制 RGB 小灯闪烁

SWITCH_IN = 12

R = 16
G = 20
B = 21

pins = {'pin_R': R, 'pin_G': G, 'pin_B': B}


# 启动相关操作
def init():
    GPIO.setwarnings(False)
    # 启用GPIO.BCM编号(不同版本的树莓派不一样); 还有一种GPIO.BOARD(不用看接口图,数引脚1~40就可以接线)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SWITCH_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # init rgb led
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.LOW)


def pinsOutput(stream):
    for i in pins:
        GPIO.output(pins[i], stream)
    time.sleep(3)


# 循环相关操作
def loop():
    while True:
        if GPIO.input(SWITCH_IN):
            pinsOutput(GPIO.HIGH)
        else:
            pinsOutput(GPIO.LOW)


def off():
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)


# 销毁操作
def destroy():
    off()
    GPIO.cleanup()


# Main程序
if __name__ == "__main__":
    try:
        init()
        loop()
    except KeyboardInterrupt:
        destroy()
