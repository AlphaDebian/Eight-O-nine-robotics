#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import time
import math
from std_msgs.msg import Float64
from bot_control import base

def callback(msg):
    b.gripper(-2.0)
    b.sweeper(1.5)
    l = round(msg.ranges[0], 3)
    m = round(min(msg.ranges[270:400]),3)
    print((msg.ranges).index(min(msg.ranges[270:400])))
    r = round(msg.ranges[719],3)
    print(l,m,r)
    if m>2.000:
        print("b.wheel_f()")
        b.wheel_f(pub,msg1)
    else:
        b.wheel_r(pub,msg1)

rospy.init_node('move',anonymous=True)
b = base()
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
msg1 = Twist()
sub = rospy.Subscriber('/Art/laser/scan', LaserScan, callback, queue_size=1)
rospy.spin()
