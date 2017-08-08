#!/usr/bin/env python

import rospy
import datetime
from pibot import srv


def get_time():
    try:
        rospy.wait_for_service('srv_clock', timeout=3)
    except rospy.ROSException:
        rospy.logerr('404: srv_clock not found')
        return None
    f = rospy.ServiceProxy('srv_clock', srv.clock)
    try:
        res = f()
    except rospy.ServiceException as err:
        rospy.logerr('500: srv_clock did not response --- %s' % (err))
        return None
    return datetime.datetime(res.year, res.month, res.day, res.hour, res.minute, res.second)


if __name__ == '__main__':
    res = get_time()
    if res:
        print(res.strftime('%Y-%m-%d %a %H:%M:%S'))
    else:
        print('Error occurred')

