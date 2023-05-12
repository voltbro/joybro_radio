#! /usr/bin/env python3
import serial, rospy, time, BroJoystick_pb2 
from cobs import cobs
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt16

class RobotRadioControll():

    def __init__(self):
        
        self.max_linear_vel = rospy.get_param('~max_linear_vel',0.5)
        self.max_angular_vel = rospy.get_param('~max_angular_vel',1.75)
        self.threshold = rospy.get_param('~threshold',20)

        self.state = 'stop'

        rospy.on_shutdown(self.on_shutdown)

        self.ser = serial.Serial()
        self.ser.baudrate = rospy.get_param('~baudrate', 19200)
        self.ser.port = rospy.get_param('~device','/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0')
        self.ser.dtr = False
        self.ser.timeout = 0.1
        self.ser.open()

        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=5)   
        self.servo44_pub = rospy.Publisher("/servo44", UInt16, queue_size=5)
        self.servo45_pub = rospy.Publisher("/servo45", UInt16, queue_size=5)

        rospy.loginfo("RobotRadioControll Init done")

    def on_shutdown(self):
        
        rospy.loginfo("Shutdown controll")
        self.cmd_vel_pub.publish(Twist()) 
        rospy.sleep(0.5) 

    def run(self):

        rospy.loginfo("Start Robot Radio Teleop")
        
        while not rospy.is_shutdown():

            pack = self.ser.read_until(b'\x00')
            pack = pack[:-1]

            try:
                proto_data = cobs.decode(pack)

                joy_proto = BroJoystick_pb2.BroJoystick()
                joy_proto.ParseFromString(proto_data)

                # True если нажато, нужно ехать

                if (joy_proto.sw1 == False and self.state == 'move'):
                    rospy.loginfo("Swith to stop state")
                    self.state = 'stop' 
                    self.cmd_vel_pub.publish(Twist())
                                     

                if (joy_proto.sw1 == True and self.state == 'stop'):
                    rospy.loginfo("Swith to move state")
                    self.state = 'move'

                linear_vel = 0
                angular_vel = 0
                
                if abs(joy_proto.LeftJoy_Y - 512) > self.threshold:
                    linear_vel = (((joy_proto.LeftJoy_Y - 512)/512.0)*self.max_linear_vel)*(joy_proto.LeftSlider/1024)

                if abs(joy_proto.LeftJoy_X - 512) > self.threshold:    
                    angular_vel = -(((joy_proto.LeftJoy_X - 512)/512.0)*self.max_angular_vel)*(joy_proto.LeftSlider/1024)

                if (self.state == 'move'):
                    twist = Twist()
                    twist.linear.x = linear_vel
                    twist.angular.z = angular_vel
                    self.cmd_vel_pub.publish(twist)     

                self.servo44_pub.publish(180 - int(joy_proto.RightJoy_X/5.8)) 
                servo45_pose = int(joy_proto.RightJoy_Y/10.3)
                print(servo45_pose)
                self.servo45_pub.publish(servo45_pose)           

            
            except :
                pass        



if __name__ == '__main__':
    rospy.init_node('radio_teleop', anonymous=True)
    teleop = RobotRadioControll()
    teleop.run();

