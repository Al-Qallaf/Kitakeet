#!/usr/bin/python
import time
import Adafruit_DHT
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

sensor_type = Adafruit_DHT.AM2302
pin = 23


while ( True ):
      humidity, temperature = Adafruit_DHT.read_retry(sensor_type, pin)

      if (humidity != None) and (temperature != None):
          #print ('{0:0.1f}*C'.format(temperature))
          #print ('{0:0.1f}%'.format(humidity))
          print ('Temp={0:0.1f}*C  Humidity={1:0.1f}%').format(temperature, humidity)
          if ((temperature >= 36 and temperature <= 37.5) or (temperature > 37.5)):
              print ('Ok, needed by Egg')
              GPIO.output(20, GPIO.HIGH)
          else:
              print ('Adjusting temperature...')
              GPIO.output(20, GPIO.LOW)
      else:
          print ('Failed to get reading.')
      time.sleep(3)
