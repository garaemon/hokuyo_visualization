#!/usr/bin/env python

import rospy

from jsk_recognition_msgs.msg import PolygonArray
from geometry_msgs.msg import Polygon, PolygonStamped, Point32
from math import cos, sin, pi
import numpy as np

if __name__ == "__main__":
    rospy.init_node("hokuyo_fov")
    pub = rospy.Publisher("/hokuyo_fov", PolygonArray)
    r = rospy.Rate(1)
    radius = 0.5
    start_theta = - 3.0 / 4.0 * pi - pi/2
    end_theta = 3.0 / 4.0 * pi - pi/2
    while not rospy.is_shutdown():
        now = rospy.Time.now()
        polygon_array = PolygonArray()
        polygon_stamped = PolygonStamped()
        
        polygon_array.header.frame_id = "hokuyo"
        polygon_array.header.stamp = now
        polygon_stamped.header.frame_id = "hokuyo"
        polygon_stamped.header.stamp = now
        polygon_stamped.polygon.points = [Point32(x=radius*cos(theta), y=radius*sin(theta))
                                          for theta in np.arange(start_theta, end_theta, 0.1)]
        polygon_stamped.polygon.points = [Point32()] + polygon_stamped.polygon.points + [Point32()]
        polygon_array.polygons.append(polygon_stamped)
        pub.publish(polygon_array)
        r.sleep()
