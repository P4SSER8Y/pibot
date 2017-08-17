#!/usr/bin/env python

import rospy
from pymongo import MongoClient
from pibot import msg

global collection 

def callback(data):
    global collection
    collection.insert({'timestamp': data.timestamp,
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

