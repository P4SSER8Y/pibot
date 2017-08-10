#!/usr/bin/env python

import rospy
import datetime
from pibot import srv

def get_cpu_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000.0
    file.close()
    return temp


def handle_system_server(request):
    response = srv.systemResponse()
    now = datetime.datetime.now()
    response.second = now.second
    response.minute = now.minute
    response.hour = now.hour
    response.day = now.day
    response.month = now.month
    response.year = now.year
    response.cpu_temp = get_cpu_temp()
    return response


def init_system_server():
    rospy.init_node('srv_system')
    s = rospy.Service('srv_system', srv.system, handle_system_server)
    rospy.loginfo('srv_system initialized')


if __name__ == '__main__':
    init_system_server()
    rospy.spin()

