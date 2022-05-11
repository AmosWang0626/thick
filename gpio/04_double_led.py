#!/usr/bin/env python
import time

import RPi.GPIO as GPIO

pin_red = 19
pin_yellow = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_red, GPIO.OUT)
GPIO.setup(pin_yellow, GPIO.OUT)


def show():
    while True:
        # 亮红 + 暗黄 = 红
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_yellow, GPIO.LOW)
        time.sleep(1)

        # 亮红 + 黄 = 橙
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_yellow, GPIO.HIGH)
        time.sleep(1)

        # 亮黄 + 暗红 = 黄
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_yellow, GPIO.HIGH)
        time.sleep(1)

        # 暗红 + 黄 = 非亮橙
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_yellow, GPIO.LOW)
        time.sleep(1)


def destroy():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_yellow, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        show()
    except KeyboardInterrupt:
        destroy()
