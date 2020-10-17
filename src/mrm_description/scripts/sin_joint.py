#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def sin_joint():
    comm = rospy.Publisher('/mrm/joint2_position_controller/command', 
                            Float64, 
                            queue_size=10)
    rospy.init_node('single_joint', anonymous=True)
    rate = rospy.Rate(60) # 10hz
    t0 = rospy.get_rostime()
    while not rospy.is_shutdown():
        rospy.sleep(1)

        x=0.3
        rospy.loginfo(x)
        comm.publish(x)
        rospy.sleep(3)

        x=0.7
        rospy.loginfo(x)
        comm.publish(x)
        rospy.sleep(3)

        x=0.1
        rospy.loginfo(x)
        comm.publish(x)
        rospy.sleep(3)

        x=0.5
        rospy.loginfo(x)
        comm.publish(x)
        rospy.sleep(3)

        x=0.0
        rospy.loginfo(x)
        comm.publish(x)
        rospy.sleep(3)
        break

if __name__ == '__main__':
    try:
        sin_joint()
    except rospy.ROSInterruptException:
        pass