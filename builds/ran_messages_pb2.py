# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ran_messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12ran_messages.proto\"\x89\x01\n\x13RAN_param_map_entry\x12\x1b\n\x03key\x18\x01 \x02(\x0e\x32\x0e.RAN_parameter\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x1d\n\x07ue_list\x18\x04 \x01(\x0b\x32\n.ue_list_mH\x00\x42\x07\n\x05value\"?\n\x16RAN_indication_request\x12%\n\rtarget_params\x18\x01 \x03(\x0e\x32\x0e.RAN_parameter\"B\n\x17RAN_indication_response\x12\'\n\tparam_map\x18\x01 \x03(\x0b\x32\x14.RAN_param_map_entry\"E\n\x13RAN_control_request\x12.\n\x10target_param_map\x18\x01 \x03(\x0b\x32\x14.RAN_param_map_entry\"\xea\x01\n\x0bRAN_message\x12#\n\x08msg_type\x18\x01 \x02(\x0e\x32\x11.RAN_message_type\x12\x39\n\x16ran_indication_request\x18\x02 \x01(\x0b\x32\x17.RAN_indication_requestH\x00\x12;\n\x17ran_indication_response\x18\x03 \x01(\x0b\x32\x18.RAN_indication_responseH\x00\x12\x33\n\x13ran_control_request\x18\x04 \x01(\x0b\x32\x14.RAN_control_requestH\x00\x42\t\n\x07payload\"\xcf\x02\n\tue_info_m\x12\x0c\n\x04rnti\x18\x01 \x02(\x03\x12\x14\n\x0c\x64lsch_errors\x18\x02 \x02(\x03\x12\x19\n\x11\x64lsch_total_bytes\x18\x03 \x02(\x03\x12\x1b\n\x13\x64lsch_current_bytes\x18\x04 \x02(\x03\x12\x14\n\x0culsch_errors\x18\x05 \x02(\x03\x12\x1c\n\x14ulsch_total_bytes_rx\x18\x06 \x02(\x03\x12\x15\n\rnum_rsrp_meas\x18\x07 \x02(\x03\x12\x16\n\x0esched_ul_bytes\x18\x08 \x02(\x03\x12\x1b\n\x13\x65stimated_ul_buffer\x18\t \x02(\x03\x12\x17\n\x0fnum_total_bytes\x18\n \x02(\x03\x12\x10\n\x08raw_rssi\x18\x0b \x02(\x03\x12\x14\n\x0cpusch_snrx10\x18\x0c \x02(\x03\x12\x14\n\x0cpucch_snrx10\x18\r \x02(\x03\x12\x0f\n\x07ul_rssi\x18\x0e \x02(\x03\"?\n\tue_list_m\x12\x15\n\rconnected_ues\x18\x01 \x02(\x05\x12\x1b\n\x07ue_info\x18\x02 \x03(\x0b\x32\n.ue_info_m*v\n\x10RAN_message_type\x12\x10\n\x0cSUBSCRIPTION\x10\x01\x12\x16\n\x12INDICATION_REQUEST\x10\x02\x12\x17\n\x13INDICATION_RESPONSE\x10\x03\x12\x0b\n\x07\x43ONTROL\x10\x04\x12\x12\n\x0eSOMETHING_ELSE\x10\x05*7\n\rRAN_parameter\x12\n\n\x06GNB_ID\x10\x01\x12\r\n\tSOMETHING\x10\x02\x12\x0b\n\x07UE_LIST\x10\x03')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ran_messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RAN_MESSAGE_TYPE._serialized_start=1006
  _RAN_MESSAGE_TYPE._serialized_end=1124
  _RAN_PARAMETER._serialized_start=1126
  _RAN_PARAMETER._serialized_end=1181
  _RAN_PARAM_MAP_ENTRY._serialized_start=23
  _RAN_PARAM_MAP_ENTRY._serialized_end=160
  _RAN_INDICATION_REQUEST._serialized_start=162
  _RAN_INDICATION_REQUEST._serialized_end=225
  _RAN_INDICATION_RESPONSE._serialized_start=227
  _RAN_INDICATION_RESPONSE._serialized_end=293
  _RAN_CONTROL_REQUEST._serialized_start=295
  _RAN_CONTROL_REQUEST._serialized_end=364
  _RAN_MESSAGE._serialized_start=367
  _RAN_MESSAGE._serialized_end=601
  _UE_INFO_M._serialized_start=604
  _UE_INFO_M._serialized_end=939
  _UE_LIST_M._serialized_start=941
  _UE_LIST_M._serialized_end=1004
# @@protoc_insertion_point(module_scope)
