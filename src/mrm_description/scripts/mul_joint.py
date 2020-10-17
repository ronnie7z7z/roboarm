#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def mul_joint():
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

    rospy.init_node('multiple_joint', anonymous=True)
    rate = rospy.Rate(60) # 10hz
    t0 = rospy.get_rostime()
    while not rospy.is_shutdown():
        rospy.sleep(1)

        a=1.2 
        b=0.4 
        c=0.2
        d=0.6
        e=0 
        rospy.loginfo("Command 1")
        comm1.publish(a)
        comm2.publish(b)
        comm3.publish(c)
        comm4.publish(d)
        comm5.publish(e)
        rospy.sleep(3)

        a=2.3 
        b=0.1 
        c=0.6
        d=0.1
        e=0 
        rospy.loginfo("Command 2")
        comm1.publish(a)
        comm2.publish(b)
        comm3.publish(c)
        comm4.publish(d)
        comm5.publish(e)
        rospy.sleep(3)

        a=0.12 
        b=0.2 
        c=0.9
        d=0.5
        e=0 
        rospy.loginfo("Command 3")
        comm1.publish(a)
        comm2.publish(b)
        comm3.publish(c)
        comm4.publish(d)
        comm5.publish(e)
        rospy.sleep(3)

        a=-2 
        b=0.4 
        c=0.6
        d=0.7
        e=0 
        rospy.loginfo("Command 4")
        comm1.publish(a)
        comm2.publish(b)
        comm3.publish(c)
        comm4.publish(d)
        comm5.publish(e)
        rospy.sleep(3)

        a=-2 
        b=0.4 
        c=0.6
        d=0.7
        e=0.4 
        rospy.loginfo("Command 5")
        comm1.publish(a)
        comm2.publish(b)
        comm3.publish(c)
        comm4.publish(d)
        comm5.publish(e)
        rospy.sleep(3)

        break

if __name__ == '__main__':
    try:
        mul_joint()
    except rospy.ROSInterruptException:
        pass