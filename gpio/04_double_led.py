#!/usr/bin/env python
import random
import time

import RPi.GPIO as GPIO

Rpin = 18
Gpin = 23

SWITCH_OBJ = {'val': False}


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Rpin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Gpin, GPIO.OUT, initial=GPIO.HIGH)


def Led(x):
    if x:
        GPIO.output(Rpin, GPIO.HIGH)
        GPIO.output(Gpin, GPIO.LOW)
    else:
        GPIO.output(Rpin, GPIO.LOW)
        GPIO.output(Gpin, GPIO.HIGH)


def loop():
    while True:
        Led(random.randint(0, 1))
        time.sleep(0.5)


def destroy():
    GPIO.output(Gpin, GPIO.HIGH)
    GPIO.output(Rpin, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
