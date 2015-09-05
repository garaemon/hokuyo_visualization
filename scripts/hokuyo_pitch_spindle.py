#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, TwistStamped

if __name__ == "__main__":
    rospy.init_node("hokuyo_pitch")
    pub = rospy.Publisher("/hokuyo_pitch", TwistStamped)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = TwistStamped()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "hokuyo"
        msg.twist.angular.x = -0.2
        pub.publish(msg)
        r.sleep()
