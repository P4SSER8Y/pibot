#!/usr/bin/env python

import rospy
from pibot import msg
from RPi import GPIO
import time

ts = 0
pub = None

def handler(pin):
    global ts
    global pub
    tmp = time.time()
    res = msg.touchpad()
    if GPIO.input(pin) == 1:
        res.value = 0
    else:
        res.value = 1
    res.width = tmp - ts
    pub.publish(res)
    ts = tmp

def init():
    pin = rospy.get_param('/pibot/pins/Touchpad')

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback = handler)

    rospy.init_node('touchpad')
    global pub
    pub = rospy.Publisher('/pibot/touchpad', msg.touchpad, queue_size=10)


if __name__ == '__main__':
    ts = time.time()
    init()
    rospy.spin()
        
