#!/usr/bin/env python

import rospy
import time
from pibot import msg
from std_msgs.msg import String

code_buff = ""
pub = None
flag = False
flag_ts = 0

morse_dict = {
        '.-'    : 'A', '-...'  : 'B', '-.-.'  : 'C', '-..'   : 'D', '.'     : 'E',
        '..-.'  : 'F', '--.'   : 'G', '....'  : 'H', '..'    : 'I', '.---'  : 'J',
        '-.-'   : 'K', '.-..'  : 'L', '--'    : 'M', '-.'    : 'N', '---'   : 'O',
        '.--.'  : 'P', '--.-'  : 'Q', '.-.'   : 'R', '...'   : 'S', '-'     : 'T',
        '..-'   : 'U', '...-'  : 'V', '.--'   : 'W', '-..-'  : 'X', '-.--'  : 'Y',
        '--..'  : 'Z',
        '-----' : '0', '.----' : '1', '..---' : '2', '...--' : '3', '....-' : '4',
        '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8', '----.' : '9',
        'enter' : 'enter',
        'backspace': 'backspace',
        'clear' : 'clear'
        }


def decode(data):
    global pub
    if data != '':
        pub.publish(morse_dict.get(data, 'unknown'))


def handler(data):
    global code_buff
    global flag
    global flag_ts
    if data.value == 0:
        flag = False
    else:
        flag_ts = time.time() + 0.5
        flag = True
        if data.width <= 0.15:
            code_buff = code_buff + '.'
        elif data.width <= 0.5:
            code_buff = code_buff + '-'
        elif data.width <= 3.0:
            decode(code_buff)
            code_buff = ''
            decode('enter')
        else:
            decode('clear')
            code_buff = ''

def init():
    global code_buff
    global char_buff
    global pub
    code_buff = ''
    char_buff = ''
    rospy.init_node('morse_decoder')
    pub = rospy.Publisher('/pibot/key', String, queue_size=32)
    rospy.Subscriber('/pibot/touchpad', msg.touchpad, handler)


def main():
    global code_buff
    global flag
    global flag_ts
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if flag and (time.time() > flag_ts):
            decode(code_buff)
            code_buff = ''
            flag = False
        rate.sleep()


if __name__ == "__main__":
    init()
    main()

