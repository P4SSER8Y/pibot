#!/usr/bin/env python

import rospy
from time import time
from pibot import srv
import Adafruit_DHT as dht


class AM2302:
    def __init__(self, pin):
        self.pin = pin
        self.timestamp = -1
        self.temperature = 0
        self.humidity = 0
        self.read()

    def handler(self, req):
        res = srv.am2302Response()
        res.timestamp = self.timestamp
        res.temperature = self.temperature
        res.humidity = self.humidity
        return res

    def read(self):
        h, t = dht.read(dht.AM2302, self.pin)
        if (t is not None) and (h is not None):
            self.timestamp = time()
            self.temperature = t
            self.humidity = h 

def main():
    rospy.init_node('sensor_am2302')

    pin = rospy.get_param('/pibot/pins/AM2302')
    sensor = AM2302(pin)
    rospy.loginfo('AM2302 @%s' % pin)

    s = rospy.Service('srv_am2302', srv.am2302, lambda req: sensor.handler(req)) 

    rate = rospy.Rate(1.0/30)
    while not rospy.is_shutdown():
        rate.sleep()
        sensor.read()
        rospy.loginfo('tick')


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

