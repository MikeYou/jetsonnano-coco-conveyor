import board
import digitalio
import busio


import time



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
        if value == True:
            i = i + t
            print(f"{i:.2f}","LOW，偵測範圍內沒人")
        elif value == False:
            i = i + t
            print(f"{i:.2f}","HIGH，有人在偵測範圍內")
finally:
    GPIO.cleanup()
