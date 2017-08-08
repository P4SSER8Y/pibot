#!/usr/bin/env python

import rospy
import datetime
from pibot import srv

def handle_clock_server(request):
    response = srv.clockResponse()
    now = datetime.datetime.now()
    response.second = now.second
    response.minute = now.minute
    response.hour = now.hour
    response.day = now.day
    response.month = now.month
    response.year = now.year
    return response


def init_clock_server():
    rospy.init_node('clock_server')
    s = rospy.Service('clock_server', srv.clock, handle_clock_server)
    rospy.loginfo('clock_server initialized')


if __name__ == '__main__':
    init_clock_server()
    rospy.spin()

