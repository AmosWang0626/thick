#!/usr/bin/env python
import time

import RPi.GPIO as GPIO

pin_red = 19
pin_yellow = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_red, GPIO.OUT)
GPIO.setup(pin_yellow, GPIO.OUT)

pwm_red = GPIO.PWM(pin_red, 100)  # 100Hz frequency
pwm_yellow = GPIO.PWM(pin_yellow, 100)  # 100Hz frequency
dc = 0
delaySec = 0.1
pwm_red.start(dc)
pwm_yellow.start(dc)


def show():
    while True:
        # 亮红
        for i in range(0, 101, 5):
            pwm_red.ChangeDutyCycle(i)
            time.sleep(delaySec)

        # 暗红
        for i in range(100, -5, -5):
            pwm_red.ChangeDutyCycle(i)
            time.sleep(delaySec)

        # 亮黄
        for i in range(0, 101, 5):
            pwm_yellow.ChangeDutyCycle(i)
            time.sleep(delaySec)

        # 暗黄
        for i in range(100, -5, -5):
            pwm_yellow.ChangeDutyCycle(i)
            time.sleep(delaySec)

        # 双色
        for i in range(0, 101, 5):
            pwm_yellow.ChangeDutyCycle(i)
            pwm_red.ChangeDutyCycle(100 - i)
            time.sleep(delaySec)

        # 双色
        for i in range(100, -5, -5):
            pwm_yellow.ChangeDutyCycle(i)
            pwm_red.ChangeDutyCycle(100 - i)
            time.sleep(delaySec)

        # 双色
        for i in range(100, -5, -5):
            pwm_red.ChangeDutyCycle(i)
            pwm_yellow.ChangeDutyCycle(100 - i)
            time.sleep(delaySec)

        # 双色
        for i in range(0, 101, 5):
            pwm_red.ChangeDutyCycle(i)
            pwm_yellow.ChangeDutyCycle(100 - i)
            time.sleep(delaySec)


def destroy():
    pwm_red.stop()
    pwm_yellow.stop()
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_yellow, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        show()
    except KeyboardInterrupt:
        destroy()
