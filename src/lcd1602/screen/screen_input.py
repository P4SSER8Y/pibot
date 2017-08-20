#!/usr/bin/env python

import time

import rospy
from pibot import msg
from std_msgs.msg import String

pub_win = None
pub_cmd = None
prior = 16
buff = ''
cmd = ''
timeout = 0


def handler(data):
    global pub_win
    global pub_cmd
    global buff
    global cmd
    global timeout

    timeout = time.time() + 3

    if data.data == 'none':
        pass
    elif data.data == 'enter':
        if len(buff) > 0:
            cmd = buff
            buff = ''
            pub_cmd.publish(String(cmd))
    elif data.data == 'clear':
        buff = ''
        cmd = ''
    elif len(data.data) == 1:
        buff = buff + data.data
    else:
        buff = buff + '{' + data.data + '}'
    m = msg.window()
    m.prior = prior
    m.timeout = 3
    m.id = 'input'
    m.content = '>' + '{: <15s}'.format(buff[-15:]) + '\n' + '{: <16s}'.format(cmd[:16])
    pub_win.publish(m) 


def init():
    rospy.init_node('screen_input')

    global pub_win
    global pub_cmd
    pub_win = rospy.Publisher('/pibot/windows', msg.window, queue_size=1)
    pub_cmd = rospy.Publisher('/pibot/command', String, queue_size=5)
    sub = rospy.Subscriber('/pibot/key', String, handler) 


if __name__ == '__main__':
    init()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
        if time.time() > timeout:
            buff = ''


