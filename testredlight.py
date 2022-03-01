import RPi.GPIO as GPIO
import time


# 設定PIN腳控制模式
GPIO.setmode(GPIO.BOARD)
# 設定要操作的PIN腳
input_pin = 18
# 設定要操作的PIN腳為輸入還是輸出
GPIO.setup(input_pin, GPIO.IN)
print("Set redl 18 as input!" )

GPIO.setwarnings(False)

i = 0 # 計算秒數
t = 0.5
try:
    while True:
        time.sleep(t)
        value = GPIO.input(input_pin)

        #if value == GPIO.HIGH:
        #    print("HIGH，偵測範圍內沒人")
        #elif value == GPIO.LOW:
        #    print("LOW，有人在偵測範圍內")
        if value == GPIO.LOW:
            i = i + t
            print(f"{i:.2f}","LOW，有人在偵測範圍內")
        elif value == GPIO.HIGH:
            i = i + t
            print(f"{i:.2f}","HIGH，偵測範圍內沒人")
finally:
    GPIO.cleanup()
