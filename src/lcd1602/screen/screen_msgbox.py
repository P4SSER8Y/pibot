#!/usr/bin/env python

import rospy
from pibot import srv, msg
from std_msgs.msg import String


pub = None
prior = 24


def handler(req):
    global pub
    m = msg.window()
    m.prior = prior
    m.timeout = req.timeout
    m.content = req.message
    m.id = 'msgbox'
    pub.publish(m)
    return True


def init():
    rospy.init_node('screen_msgbox')

    global pub
    global sub
    pub = rospy.Publisher('/pibot/windows', msg.window, queue_size=1)
    s = rospy.Service('srv_msgbox', srv.msgbox, handler)


if __name__ == '__main__':
    init()
    rospy.spin()

