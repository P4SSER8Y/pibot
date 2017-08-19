#!/usr/bin/env python

import rospy
from pibot import msg
import time

prior = 1
s_temp = ' H:XX.X  T:XX.X '

def handler_temp(data):
    global s_temp
    s_temp = " H:{0: >-2.1f}  T:{1: >-2.1f} ".format(data.humidity, data.temperature)


if __name__ == '__main__':
    rospy.init_node('screen_clock')
    pub = rospy.Publisher('/pibot/windows', msg.window, queue_size=1)
    sub_temp = rospy.Subscriber('/pibot/air', msg.air, handler_temp)
    rate = rospy.Rate(1)
    m = msg.window()
    m.prior = prior
    m.id = 'clock'
    m.timeout = 0

    while not rospy.is_shutdown():
        s_datetime = time.strftime(" %m-%d %H:%M:%S ")
        m.content = s_datetime + '\n' + s_temp
        pub.publish(m)
        rate.sleep()

