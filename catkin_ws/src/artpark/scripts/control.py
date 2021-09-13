#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def sweeper(x):
    pub = rospy.Publisher('/Art/sweeper_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = "hello world %s" % rospy.get_time()
    position = x
    rospy.loginfo(position)
    pub.publish(position)
    rate.sleep()

def foam(x):
    pub = rospy.Publisher('/Art/foam_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = "hello world %s" % rospy.get_time()
    position = x
    rospy.loginfo(position)
    pub.publish(position)
    rate.sleep()

def gripper(x):
    pub = rospy.Publisher('/Art/gripper_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = "hello world %s" % rospy.get_time()
    position = -x
    rospy.loginfo(position)
    pub.publish(position)
    rate.sleep()

def wheel(x):
    pub = rospy.Publisher('/Art/wheel1_position_controller/command', Float64, queue_size=10)
    pub1 = rospy.Publisher('/Art/wheel2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = "hello world %s" % rospy.get_time()
    position = -x
    rospy.loginfo(position)
    pub.publish(position)
    pub1.publish(position)
    rate.sleep()

if __name__ == '__main__':
    x = 0.0
    while not rospy.is_shutdown():
        try:
            sweeper(x)
            foam(x)
            gripper(x)
            x += 0.1
        except rospy.ROSInterruptException:
            pass