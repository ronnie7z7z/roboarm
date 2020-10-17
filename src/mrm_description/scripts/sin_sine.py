#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def sin_single():
    comm = rospy.Publisher('/mrm/joint5_position_controller/command', 
                            Float64, 
                            queue_size=10)
    rospy.init_node('sine_single', anonymous=True)
    rate = rospy.Rate(60) # 10hz
    while not rospy.is_shutdown():
        x = 0.2 + 0.2*math.sin(float(rospy.get_time()))
        comm.publish(x)
        rate.sleep()

if __name__ == '__main__':
    try:
        sin_single()
    except rospy.ROSInterruptException:
        pass