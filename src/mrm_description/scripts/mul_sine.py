#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def sin_multiple():
    comm1 = rospy.Publisher('/mrm/joint1_position_controller/command', 
                            Float64, 
                            queue_size=10)
    comm2 = rospy.Publisher('/mrm/joint2_position_controller/command', 
                            Float64, 
                            queue_size=10)
    comm3 = rospy.Publisher('/mrm/joint3_position_controller/command', 
                            Float64, 
                            queue_size=10)
    comm4 = rospy.Publisher('/mrm/joint4_position_controller/command', 
                            Float64, 
                            queue_size=10)
    comm5 = rospy.Publisher('/mrm/joint5_position_controller/command', 
                            Float64, 
                            queue_size=10)
    rospy.init_node('sine_multiple', anonymous=True)
    rate = rospy.Rate(60) # 10hz
    while not rospy.is_shutdown():
        a = 1.5*math.sin(float(rospy.get_time()))
        b = 0.3 + 0.3*math.sin(float(rospy.get_time())+3.2)
        c = 0.4 + 0.4*math.sin(float(rospy.get_time())-1)
        d = 0.5 + 0.2*math.sin(float(rospy.get_time())+3.14)
        e = 3*math.sin(float(rospy.get_time())+1.57)
        #rospy.loginfo()
        comm1.publish(a)
        comm2.publish(b)
        comm3.publish(c)
        comm4.publish(d)
        comm5.publish(e)
        rate.sleep()

if __name__ == '__main__':
    try:
        sin_multiple()
    except rospy.ROSInterruptException:
        pass