#! /usr/bin/python

import serial, rospy, signal, BroJoystick_pb2 
from cobs import cobs
from joybro.msg import JoyBro

global_loop = True
rospy.init_node('joy_serial_node', anonymous=True)

# /dev/tty.SLAB_USBtoUART
serial_device = rospy.get_param('~device','/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0')
baudrate = rospy.get_param('~baudrate', 9600)
pub_topic = rospy.get_param('~pub_topic','/joybro')

rospy.loginfo("Start Radio reciver")
rospy.loginfo("Radio device: %s", serial_device)
rospy.loginfo("Radio baudrate: %s", baudrate)
rospy.loginfo("Pub topic: %s", pub_topic)


ser = serial.Serial(port=serial_device, 
        baudrate=baudrate, 
        timeout=0.1, 
        dsrdtr=True)

pub = rospy.Publisher(pub_topic, JoyBro, queue_size=5)        

def get_topic(joy_proto):

    joy_topic = JoyBro()

    joy_topic.left_x = joy_proto.LeftJoy_X - 512
    joy_topic.left_y = joy_proto.LeftJoy_Y - 512
    joy_topic.right_x = joy_proto.RightJoy_X - 512
    joy_topic.right_y = joy_proto.RightJoy_Y - 512

    joy_topic.btn1 = joy_proto.btn1
    joy_topic.btn2 = joy_proto.btn2
    joy_topic.btn3 = joy_proto.btn3
    joy_topic.btn4 = joy_proto.btn4

    joy_topic.sw1 = joy_proto.sw1
    joy_topic.sw2 = joy_proto.sw2

    joy_topic.slider1 = joy_proto.LeftSlider
    joy_topic.slider2 = joy_proto.RightSlider

    return joy_topic

def stop_global_loop(signal, frame):
    global global_loop
    print("Ctrl+C captured, ending read.")
    global_loop = False

signal.signal(signal.SIGINT, stop_global_loop)

while global_loop:
    pack = ser.read_until(b'\x00')
    pack = pack[:-1]

    try:
        proto_data = cobs.decode(pack)

        joy_proto = BroJoystick_pb2.BroJoystick()
        joy_proto.ParseFromString(proto_data)

        joy_topic = get_topic(joy_proto)
        pub.publish(joy_topic)

    except :
        pass

rospy.loginfo("Stop Radio reciver")
ser.close()