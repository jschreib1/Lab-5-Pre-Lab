import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pwmPin = 24
GPIO.setup(pwmPin, GPIO.OUT)
# set min & max % duty cycles (5 and 10 are default values, but play
# around to find optimum values for your motor)
dcMin = 2
dcMax = 15
pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(0)
try:
  while True:
    for dc in range(dcMin,dcMax):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(0.5)
except KeyboardInterrupt:
  print("bye")
  GPIO.cleanup()