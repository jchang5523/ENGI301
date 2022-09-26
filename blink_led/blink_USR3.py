import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("USR%d" % 3, GPIO.OUT)

while True:
        GPIO.output("USR%d" % 3, GPIO.HIGH)
        time.sleep(0.10)
        GPIO.output("USR%d" % 3, GPIO.LOW)
        time.sleep(0.10)