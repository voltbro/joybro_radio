## How to install

### Python 
pip install -r requirements.txt

### ROS
Install pack
```
sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic --pkg=joybro_radio
```

### HC12
default speed 19200

```
AT+B19200
```

### ROS node launch files 

Start radio->joybro topic publisher
```
roslaunch joybro_radio joybro_radio.launch
```

Start radio->joybro topic publisher and `joybro` teleop node
```
roslaunch joybro_radio joybro_radio_teleop.launch
```


## Arduino

__Additional Arduino libraries__

Protobuf MicroProcessor's protocol lib https://github.com/nanopb/nanopb

PacketSerial - packets managing and COBS encoding lib https://github.com/bakercp/PacketSerial

Libraries should be installed into Arduino\Libraries\

## Protobuf 

```
protoc --nanopb_out=. BroJoystick.proto
protoc --python_out=. BroJoystick.proto
```