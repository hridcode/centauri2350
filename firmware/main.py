from machine import Pin
import utime

# Onboard LED
led = Pin(39, Pin.OUT)

while True:
    led.toggle()
    utime.sleep(0.3)