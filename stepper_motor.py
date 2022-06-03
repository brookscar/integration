from time import sleep
import RPi.GPIO as GPIO

def verticalMotorDown():
    
    DIR = 20   # Direction GPIO Pin
    STEP = 21  # Step GPIO Pin
    SPR = 2  # Steps per Revolution (360 / 1.8)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)

    MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
    GPIO.setup(MODE, GPIO.OUT)
    RESOLUTION = {'Full': (0, 0, 0),
                  'Half': (1, 0, 0),
                  '1/4': (0, 1, 0),
                  '1/8': (1, 1, 0),
                  '1/16': (1, 1, 1),
                  }
    GPIO.output(MODE, RESOLUTION['Full'])
    GPIO.output(DIR, 1)
    step_count = SPR * 32
    delay = 0.00208
    
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        
def verticalMotorUp():
    
    DIR = 20   # Direction GPIO Pin
    STEP = 21  # Step GPIO Pin
    SPR = 2  # Steps per Revolution (360 / 7.5)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, 0)

    MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
    GPIO.setup(MODE, GPIO.OUT)
    RESOLUTION = {'Full': (0, 0, 0),
                  'Half': (1, 0, 0),
                  '1/4': (0, 1, 0),
                  '1/8': (1, 1, 0),
                  '1/16': (1, 1, 1),
                  }
    GPIO.output(MODE, RESOLUTION['Full'])
    step_count = SPR * 32
    delay = 0.00208
    
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

GPIO.cleanup()

