# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BroJoystick.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BroJoystick.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x42roJoystick.proto\"\xe7\x02\n\x0b\x42roJoystick\x12\x16\n\tLeftJoy_X\x18\x01 \x02(\r:\x03\x35\x31\x32\x12\x16\n\tLeftJoy_Y\x18\x02 \x02(\r:\x03\x35\x31\x32\x12\x17\n\nRightJoy_X\x18\x03 \x02(\r:\x03\x35\x31\x32\x12\x17\n\nRightJoy_Y\x18\x04 \x02(\r:\x03\x35\x31\x32\x12\x15\n\nLeftSlider\x18\x05 \x02(\r:\x01\x30\x12\x16\n\x0bRightSlider\x18\x06 \x02(\r:\x01\x30\x12\x1a\n\x0bLeftJoy_Btn\x18\x07 \x02(\x08:\x05\x66\x61lse\x12\x1b\n\x0cRightJoy_Btn\x18\x08 \x02(\x08:\x05\x66\x61lse\x12\x13\n\x04\x62tn1\x18\t \x02(\x08:\x05\x66\x61lse\x12\x13\n\x04\x62tn2\x18\n \x02(\x08:\x05\x66\x61lse\x12\x13\n\x04\x62tn3\x18\x0b \x02(\x08:\x05\x66\x61lse\x12\x13\n\x04\x62tn4\x18\x0c \x02(\x08:\x05\x66\x61lse\x12\x12\n\x03sw1\x18\r \x02(\x08:\x05\x66\x61lse\x12\x12\n\x03sw2\x18\x0e \x02(\x08:\x05\x66\x61lse\x12\x12\n\x03sw3\x18\x0f \x02(\x08:\x05\x66\x61lse'
)




_BROJOYSTICK = _descriptor.Descriptor(
  name='BroJoystick',
  full_name='BroJoystick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='LeftJoy_X', full_name='BroJoystick.LeftJoy_X', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LeftJoy_Y', full_name='BroJoystick.LeftJoy_Y', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RightJoy_X', full_name='BroJoystick.RightJoy_X', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RightJoy_Y', full_name='BroJoystick.RightJoy_Y', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LeftSlider', full_name='BroJoystick.LeftSlider', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RightSlider', full_name='BroJoystick.RightSlider', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LeftJoy_Btn', full_name='BroJoystick.LeftJoy_Btn', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RightJoy_Btn', full_name='BroJoystick.RightJoy_Btn', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='btn1', full_name='BroJoystick.btn1', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='btn2', full_name='BroJoystick.btn2', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='btn3', full_name='BroJoystick.btn3', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='btn4', full_name='BroJoystick.btn4', index=11,
      number=12, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sw1', full_name='BroJoystick.sw1', index=12,
      number=13, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sw2', full_name='BroJoystick.sw2', index=13,
      number=14, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sw3', full_name='BroJoystick.sw3', index=14,
      number=15, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=381,
)

DESCRIPTOR.message_types_by_name['BroJoystick'] = _BROJOYSTICK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BroJoystick = _reflection.GeneratedProtocolMessageType('BroJoystick', (_message.Message,), {
  'DESCRIPTOR' : _BROJOYSTICK,
  '__module__' : 'BroJoystick_pb2'
  # @@protoc_insertion_point(class_scope:BroJoystick)
  })
_sym_db.RegisterMessage(BroJoystick)


# @@protoc_insertion_point(module_scope)