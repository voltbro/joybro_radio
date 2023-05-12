#! /usr/bin/env python3
import sys
import rospy, time 
from geometry_msgs.msg import Twist


class WhatchDog():
    def __init__(self) -> None:
        self.sub = rospy.Subscriber("/cmd_vel", Twist, self.callback)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=5)
        self.last_call = self.milli_time() 
        self.cmd_vel = Twist()

    def callback(self, data:Twist):
        self.last_call = self.milli_time()
        self.cmd_vel = data

    def run(self, timeout_ms:int = 2000) -> None:
        rospy.loginfo(f"Start WhatchDog with: {timeout_ms}ms")

        while not rospy.is_shutdown():
            rospy.sleep(0.1)

            now_time = self.milli_time()
            if (now_time - self.last_call > timeout_ms):

                if (round(self.cmd_vel.linear.x, 2) !=0 
                        or round(self.cmd_vel.angular.z, 2) != 0):
                
                    rospy.loginfo(f"WhatchDog stop robot: {now_time}")
                    self.pub.publish(Twist())

    def milli_time(self) -> int:
        return round(time.time() * 1000)
    

if __name__ == '__main__':
    try:
        rospy.init_node('simple_whatch_dog')
        dog = WhatchDog()
        dog.run(rospy.get_param('~timeout_ms', 2000))
        
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)        