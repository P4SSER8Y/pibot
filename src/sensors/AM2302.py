#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('sensor_am2302')
    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        rate.sleep()
        rospy.loginfo('tick')

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
