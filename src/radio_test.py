#! /usr/bin/python

import serial, signal, BroJoystick_pb2 
from cobs import cobs


global_loop = True
 
serial_device = "/dev/tty.usbserial-0001" 
serial_device = "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0" 
baudrate = 19200

ser = serial.Serial(port=serial_device, 
        baudrate=baudrate, 
        timeout=0.1, 
        dsrdtr=True)


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

        print(f"left x: {joy_proto.LeftJoy_X}")
        print(f"left y: {joy_proto.LeftJoy_Y}")

    except :
        pass

ser.close()