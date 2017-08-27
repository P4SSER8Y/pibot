#!/usr/bin/env python

import rospy
import pytz
from datetime import datetime
from pymongo import MongoClient
from pibot import msg

global collection 

tz = pytz.timezone('Asia/Shanghai')

def callback(data):
    global collection
    collection.insert({'time': datetime.fromtimestamp(data.timestamp).replace(tzinfo=tz),
                       'temperature': data.temperature,
                       'humidity': data.humidity})

def init():
    port = rospy.get_param('/pibot/mongodb_port')

    client = MongoClient('localhost', port)
    db = client.pibot
    global collection
    collection = db.air

    rospy.init_node('air')
    rospy.Subscriber('/pibot/air', msg.air, callback)

if __name__ == '__main__':
    init()
    rospy.spin()

