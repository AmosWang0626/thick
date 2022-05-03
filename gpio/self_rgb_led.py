#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# 自定义点亮 RGB 小灯

R = 18
G = 15
B = 14


def setup(Rpin, Gpin, Bpin):
    global pins
    global p_R, p_G, p_B
    pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)  # Set pins' mode is output

    p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
    p_G = GPIO.PWM(pins['pin_G'], 1999)
    p_B = GPIO.PWM(pins['pin_B'], 5000)

    p_R.start(100)  # Initial duty Cycle = 0(leds off)
    p_G.start(100)
    p_B.start(100)


def off():
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)  # Turn off all leds


def setColor(sleepTime):  # For example : col = 0x112233
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                p_R.ChangeDutyCycle(0 if (i == 1) else 100)
                p_G.ChangeDutyCycle(0 if (j == 1) else 100)
                p_B.ChangeDutyCycle(0 if (k == 1) else 100)
                time.sleep(sleepTime)


def loop():
    while True:
        setColor(1)


def destroy():
    p_R.stop()
    p_G.stop()
    p_B.stop()
    off()
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        setup(R, G, B)
        loop()
    except KeyboardInterrupt:
        destroy()
