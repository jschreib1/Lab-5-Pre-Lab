import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pwmPin = 16
GPIO.setup(pwmPin, GPIO.OUT)

dcMin = 0
dcMax = 100
pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(0)
try:
  for dc in range(dcMin,dcMax):
    pwm.ChangeDutyCycle(100-dc)
    print(dc)
    time.sleep(0.5)
except KeyboardInterrupt:
  print("bye")
  GPIO.cleanup()