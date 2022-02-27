import RPi.GPIO as GPIO
import time


# for 1st Motor on ENA
ENA = 13 #33
IN1 = 19#35
IN2 = 26#37
IN3 = 16#36
IN4 = 20#38
ENB = 12#32



# set pin numbers to the board's



# initialize EnA, In1 and In2
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)


# Stop
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
GPIO.output(ENB, GPIO.HIGH)
time.sleep(1)


# Forward
#GPIO.output(IN1, GPIO.HIGH)
#GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)



## Stop
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.LOW)
#GPIO.output(IN3, GPIO.LOW)
#GPIO.output(IN4, GPIO.LOW)
#time.sleep(1)


## Backward
#GPIO.output(IN1, GPIO.HIGH)
#GPIO.output(IN2, GPIO.LOW)
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.HIGH)
#time.sleep(1)

a = input("stop? (y/n)")
if a == "y":
# Stop
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(ENB, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup()
else:
    pass
