#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from pibot import msg
import time

pub = None

curr_prio = -1
curr_id = 'none'
due_time = time.time()

def handler(data):
    global curr_prio
    global curr_id
    global due_time
    if (data.prior >= curr_prio) or (time.time() >= due_time):
        curr_prio = data.prior
        due_time = time.time() + data.timeout
        pub.publish(data.content) 


def init():
    rospy.init_node('window_manager')

    global pub
    pub = rospy.Publisher('/pibot/lcd1602', String, queue_size = 10)

    sub = rospy.Subscriber('/pibot/windows', msg.window, handler)


if __name__ == '__main__':
    init()
    rospy.spin()


