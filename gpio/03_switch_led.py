#!/usr/bin/env python

import RPi.GPIO as GPIO

BtnPin = 12

Rpin = 18
Gpin = 23

SWITCH_OBJ = {'val': False}


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Rpin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Gpin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)


def Led(x):
    if x:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    else:
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)


def Print(x):
    print('***********************')
    print('*   Button Pressed!   *', x)
    print('***********************')


def detect(chn):
    if GPIO.input(BtnPin) == 0:
        SWITCH_OBJ['val'] = not SWITCH_OBJ['val']
    tempVal = SWITCH_OBJ['val']
    Led(tempVal)
    Print(tempVal)


def loop():
    while True:
        pass


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
