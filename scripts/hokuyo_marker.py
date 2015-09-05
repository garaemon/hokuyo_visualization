#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker

if __name__ == "__main__":
    rospy.init_node("hokuyo_marker")
    pub = rospy.Publisher("/hokuyo_marker", Marker)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        marker = Marker()
        marker.header.frame_id = "hokuyo"
        marker.header.stamp = rospy.Time.now()
        marker.type = Marker.MESH_RESOURCE
        marker.color.a = 1.0
        marker.color.r = 0.2
        marker.color.g = 0.2
        marker.color.b = 0.2
        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0
        marker.mesh_resource = "package://multisense_description/meshes/hokuyo_link.STL"
        marker.pose.orientation.x = 0.7
        marker.pose.orientation.w = 0.7
        pub.publish(marker)
        r.sleep()
