#!/usr/bin/env python

import rospy
from std_msgs.msg import String

from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
from time import sleep

dirs = {
    APDS9960_DIR_NONE: "none",
    APDS9960_DIR_LEFT: "left",
    APDS9960_DIR_RIGHT: "right",
    APDS9960_DIR_UP: "up",
    APDS9960_DIR_DOWN: "down",
    APDS9960_DIR_NEAR: "near",
    APDS9960_DIR_FAR: "far",
}

port = 1
bus = smbus.SMBus(port)

apds = None
pub = None

def handler(channel):
    if apds.isGestureAvailable():
        motion = apds.readGesture()
        pub.publish(dirs.get(motion, "none"))


if __name__ == "__main__":
    pin = rospy.get_param('/pibot/pins/gesture_int')
    apds = APDS9960(bus)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback = handler)

    apds.setProximityIntLowThreshold(50)

    rospy.init_node('apds9960')
    pub = rospy.Publisher('/pibot/key', String, queue_size=1)
    apds.enableGestureSensor()

    rospy.spin()

    GPIO.cleanup()

