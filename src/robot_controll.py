import serial, rospy, signal, BroJoystick_pb2 
from cobs import cobs
from geometry_msgs.msg import Twist

class RobotRadioControll():

    def __init__(self):
        
        self.max_linear_vel = rospy.get_param('~max_linear_vel',0.35)
        self.max_angular_vel = rospy.get_param('~max_angular_vel',1.5)
        self.threshold = rospy.get_param('~threshold',20)

        self.state = 'stop'

        rospy.on_shutdown(self.on_shutdown)

        self.ser = serial.Serial(port=rospy.get_param('~device','/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0'), 
            baudrate=rospy.get_param('~baudrate', 19200), 
            timeout=0.1, 
            dsrdtr=True)
        
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=5)        
        rospy.loginfo("Init done")

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

                if self.state == 'stop' and joy_proto.sw1 == 1:
                    self.state = 'move'

                if(self.state == 'move' and joy_proto.sw1 == 0):
                    twist = Twist()
                    self.pub.publish(twist)
                    self.state = 'stop'                

                if abs(joy_proto.LeftJoy_X - 512) > self.threshold:
                    linear_vel = (((joy_proto.LeftJoy_X - 512)/512.0)*self.max_linear_vel)*(joy_proto.LeftSlider/1024)

                if abs(joy_proto.LeftJoy_Y - 512) > self.threshold:    
                    angular_vel = -(((joy_proto.LeftJoy_Y - 512)/512.0)*self.max_angular_vel)*(joy_proto.LeftSlider/1024)

                if (self.state == 'move'):
                    twist = Twist()
                    twist.linear.x = linear_vel
                    twist.angular.z = angular_vel
                    self.pub.publish(twist)                

            
            except :
                pass        



if __name__ == '__main__':
    rospy.init_node('radio_teleop', anonymous=True)
    teleop = RobotRadioControll()
    teleop.run();

