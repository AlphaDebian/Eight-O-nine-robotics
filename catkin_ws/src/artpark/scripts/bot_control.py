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
class base(object):
  
    def wheel_f(self,pub,msg):
        print(msg.linear.x)
        msg.linear.x = -5.0
        print(msg.linear.x)
        msg.linear.y = 0.0
        msg.angular.z = 0.0
        rospy.loginfo(msg)
        pub.publish(msg)
        rate = rospy.Rate(10)
        # rate.sleep()
    
    def wheel_b(self,pub,msg):
        msg.linear.x = 5
        msg.linear.y = 0
        msg.angular.z = 0
        pub.publish(msg)
        rate = rospy.Rate(10)
        # rate.sleep()

    def wheel_l(self,pub,msg):
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = -0.7
        pub.publish(msg)
        rate = rospy.Rate(10)
        # rate.sleep()

    def wheel_r(self,pub,msg):
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0.7
        pub.publish(msg)
        rate = rospy.Rate(10)
        # rate.sleep()
        
    def sweeper(self, x):
        pub = rospy.Publisher('/Art/sweeper_position_controller/command', Float64, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        position = x
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

    def foam(self, x):
        pub = rospy.Publisher('/Art/foam_position_controller/command', Float64, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        position = x
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

    def gripper(self, x):
        pub = rospy.Publisher('/Art/gripper_position_controller/command', Float64, queue_size=1)
        rate = rospy.Rate(10) # 10hz
        position = x
        # rospy.loginfo(position)
        pub.publish(position)
    
    def gripperL(self, x):
        pub = rospy.Publisher('/Art/gear_left_position_controller/command', Float64, queue_size=1)
        rate = rospy.Rate(10) # 10hz
        position = x
        # rospy.loginfo(position)
        pub.publish(position)

    def gripperR(self, x):
        pub = rospy.Publisher('/Art/gear_right_position_controller/command', Float64, queue_size=1)
        rate = rospy.Rate(10) # 10hz
        position = x
        # rospy.loginfo(position)
        pub.publish(position)

    def servo(self, x):
        pub = rospy.Publisher('/Art/gripper_position_controller/command', Float64, queue_size=1)
        rate = rospy.Rate(10) # 10hz
        position = x
        # rospy.loginfo(position)
        pub.publish(position)

    def servo_l(self, x):
        pub = rospy.Publisher('/Art/ gripper_left_position_controller/command', Float64, queue_size=1)
        rate = rospy.Rate(10) # 10hz
        position = x
        # rospy.loginfo(position)
        pub.publish(position)

    def servo_r(self, x):
        pub = rospy.Publisher('/Art/ gripper_right_position_controller/command', Float64, queue_size=1)
        rate = rospy.Rate(10) # 10hz
        position = x
        # rospy.loginfo(position)
        pub.publish(position)
        