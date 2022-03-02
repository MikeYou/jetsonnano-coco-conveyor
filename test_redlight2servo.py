import board
import digitalio
import busio


import time
"""controlling servo mode PCA9685"""
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)



D24 = digitalio.DigitalInOut(board.D24)
D24.direction = digitalio.Direction.INPUT

i = 0 # 計算秒數
t = 0.5
try:
    while True:
        time.sleep(t)
        value = D24.value

        #if value == GPIO.HIGH:
        #    print("HIGH，偵測範圍內沒人")
        #elif value == GPIO.LOW:
        #    print("LOW，有人在偵測範圍內")
        if value == False:
            i = i + t
            kit.servo[8].angle=60
            kit.servo[0].angle=60
        elif value == True:
            i = i + t
            kit.servo[8].angle=90
            kit.servo[0].angle=90
finally:
    GPIO.cleanup()
