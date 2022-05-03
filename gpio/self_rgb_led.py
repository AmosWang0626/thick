#!/usr/bin/env python
import time

import RPi.GPIO as GPIO

# 自定义点亮 RGB 小灯
# https://www.yuque.com/docs/share/bdba5051-e0dc-48a1-902c-db251444c6a2?#

# 实现: 初始化为高电平输出, 然后通过改变占空比, 控制 RGB 小灯闪烁

R = 16
G = 20
B = 21


# 1. 启动相关操作(初始化)
def setup(rPin, gPin, bPin):
    global pins
    global p_R, p_G, p_B
    pins = {'pin_R': rPin, 'pin_G': gPin, 'pin_B': bPin}
    # 启用GPIO.BCM编号(不同版本的树莓派不一样); 还有一种GPIO.BOARD(不用看接口图,数引脚1~40就可以接线)
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)  # Set pins' mode is output

    # 创建一个 PWM 实例
    p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
    p_G = GPIO.PWM(pins['pin_G'], 1999)
    p_B = GPIO.PWM(pins['pin_B'], 5000)

    # 启动PWM，并初始化占空比
    p_R.start(100)  # Initial duty Cycle = 0(leds off)
    p_G.start(100)
    p_B.start(100)


# 2. 闪烁相关操作
def setColor(sleepTime):  # For example : col = 0x112233
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                # 改变占空比
                p_R.ChangeDutyCycle(0 if (i == 1) else 100)
                p_G.ChangeDutyCycle(0 if (j == 1) else 100)
                p_B.ChangeDutyCycle(0 if (k == 1) else 100)
                time.sleep(sleepTime)


def loop():
    while True:
        setColor(1)


# 停止相关操作
def off():
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)  # Turn off all leds


def destroy():
    # 停止 PWM
    p_R.stop()
    p_G.stop()
    p_B.stop()
    off()
    GPIO.cleanup()


# Main程序
if __name__ == "__main__":
    try:
        setup(R, G, B)
        loop()
    except KeyboardInterrupt:
        destroy()
