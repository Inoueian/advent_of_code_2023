import pytest

from day_16 import *

test_input_0 = 'D2FE28'
test_input_1 = '38006F45291200'
test_input_2 = 'EE00D40C823060'


def test_binary():
    packet_0 = Packet(test_input_0)
    packet_1 = Packet(test_input_1)
    assert packet_0.binary == '110100101111111000101000'
    assert packet_1.binary == '00111000000000000110111101000101001010010001001000000000'


def test_version():
    packet_0 = Packet(test_input_0)
    packet_1 = Packet(test_input_1)
    assert packet_0.version == 6
    assert packet_1.version == 1


def test_type_id():
    packet_0 = Packet(test_input_0)
    packet_1 = Packet(test_input_1)
    assert packet_0.type_id == 4
    assert packet_1.type_id == 6


def test_number():
    packet_0 = Packet(test_input_0)
    packet_1 = Packet(test_input_1)
    assert packet_0.literal == 2021
    assert packet_1.literal is None


def test_subpackets():
    packet_1 = Packet(test_input_1)
    subpackets_1 = packet_1.subpackets
    assert len(subpackets_1) == 2
    assert subpackets_1[0].literal == 10
    assert subpackets_1[1].literal == 20

    packet_2 = Packet(test_input_2)
    subpackets_2 = packet_2.subpackets
    assert len(subpackets_2) == 3
    assert subpackets_2[0].literal == 1
    assert subpackets_2[1].literal == 2
    assert subpackets_2[2].literal == 3


def test_packet_sum():
    packet_0 = Packet('8A004A801A8002F478')
    packet_1 = Packet('620080001611562C8802118E34')
    packet_2 = Packet('C0015000016115A2E0802F182340')
    packet_3 = Packet('A0016C880162017C3686B18A3D4780')
    assert packet_0.version_sum == 16
    assert packet_1.version_sum == 12
    assert packet_2.version_sum == 23
    assert packet_3.version_sum == 31


def test_evaluate():
    packet_0 = Packet('C200B40A82')
    packet_1 = Packet('04005AC33890')
    packet_2 = Packet('880086C3E88112')
    packet_3 = Packet('CE00C43D881120')
    packet_4 = Packet('D8005AC2A8F0')
    packet_5 = Packet('F600BC2D8F')
    packet_6 = Packet('9C005AC2F8F0')
    packet_7 = Packet('9C0141080250320F1802104A08')
    assert packet_0.value == 3
    assert packet_1.value == 54
    assert packet_2.value == 7
    assert packet_3.value == 9
    assert packet_4.value == 1
    assert packet_5.value == 0
    assert packet_6.value == 0
    assert packet_7.value == 1
