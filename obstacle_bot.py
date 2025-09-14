from picozero import LED,pico_led
from machine import Pin
import time
import random

#Motor
rmr=LED(10) #Right Motor Reverse
rmf=LED(11) #Right Motor Forward
lmf=LED(12) #Left Motor Forward
lmr=LED(13) #Left Motor Reverse

#Ultrasonic sensor
trig = machine.Pin(3, machine.Pin.OUT)
echo = machine.Pin(2, machine.Pin.IN) 

c = [1,2] #Random choice
gr=0.35

#Functions
def forward():
    rmf.on(gr)
    lmf.on(gr)
    
def reverse():
    rmr.on(gr)
    lmr.on(gr)
    
def right():
    rmf.off()
    lmf.on(gr)
    
def left():
    rmf.on(gr)
    lmf.off()
    
def stop():
    rmr.off()
    rmf.off()
    lmf.off()
    lmr.off()
    
    
def distance():
    trig.value(0)
    time.sleep(0.1)
    trig.value(1)
    time.sleep(0.1)
    trig.value(0)

    pulse = machine.time_pulse_us(echo, 1, 30000) # Pulse duration
    distance = (pulse * 0.0343)/2
    return distance


while True:
    pico_led.on()
    time.sleep(0.01)
    forward()
    dist=distance()
    if dist <= 7 :
        stop()
        time.sleep(0.01)
        reverse()
        time.sleep(1)
        ch=random.choice(c)
        if ch == 1:
            stop()
            time.sleep(0.03)
            right()
            time.sleep(1)
        elif ch == 2:
            stop()
            time.sleep(0.03)
            left()
            time.sleep(1)

    stop()      
    forward()
