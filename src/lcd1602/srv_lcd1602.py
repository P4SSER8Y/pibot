#!/usr/bin/env python

from Adafruit_CharLCD import Adafruit_CharLCD
import rospy
from std_msgs.msg import String

sub = None
lcd = None
buff = '  PiBot Loaded  \n  Hello World!  '

def handler(data):
    global buff
    global lcd
    lcd.setCursor(0, 0)
    lcd.write(data.data)
    buff = data.data


def init():
    global lcd
    global sub
    pins = rospy.get_param('/pibot/pins/LCD1602')
    lcd = Adafruit_CharLCD(pin_rs=pins['RS'], pin_e=pins['EN'], pins_db=pins['DATA'], GPIO=None)
    lcd.begin(16, 2)
    lcd.clear()
    lcd.write('  PiBot Loaded  \n  Hello World!  ')
    lcd.setCursor(0, 0)

    rospy.init_node('lcd1602')
    sub = rospy.Subscriber('/pibot/lcd1602', String, handler)
    

if __name__ == '__main__':
    init()
    rospy.spin()
    sub.unregister()
    lcd.clear()
    lcd.write('PiBot Shutdowned\nAuf Wiedersehen!')


