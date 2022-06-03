from time import sleep
import RPi.GPIO as GPIO

def horizontalMotorOpen():
    
    DIR = 8   # Direction GPIO Pin
    STEP = 7  # Step GPIO Pin
    SPR = 1  # Steps per Revolution (360 / 1.8)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, 0)
    
    step_count = SPR * 32
    delay = 0.0208 / 16
    
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        
def horizontalMotorClose():
    
    DIR = 8   # Direction GPIO Pin
    STEP = 7  # Step GPIO Pin
    SPR = 2  # Steps per Revolution (360 / 1.8)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, 1)

    step_count = SPR * 1
    delay = 0.0208 / 16
    
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

GPIO.cleanup()

