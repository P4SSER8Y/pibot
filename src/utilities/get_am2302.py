#!/usr/bin/env python

import rospy
import datetime
from pibot import srv


def get_am2302():
    try:
        rospy.wait_for_service('srv_am2302', timeout=3)
    except rospy.ROSException:
        rospy.logerr('404: srv_am2302 not found')
        return None
    f = rospy.ServiceProxy('srv_am2302', srv.am2302)
    try:
        res = f()
    except rospy.ServiceException as err:
        rospy.logerr('500: srv_am2302 did not response --- %s' % (err))
        return None
    return res


if __name__ == '__main__':
    res = get_am2302()
    if res:
        print(res)
    else:
        print('Error occurred')

