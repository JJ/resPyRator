import pytest

from communications import RX

def test_builds():
    rx = RX(0x0000000)
    assert rx.get("header") == 0x00
    assert rx.get(0x00) == 0x00

    rx = RX(0x0123456)
    assert rx.get("header")          == 0
    assert rx.get("protocolVersion") == 1
    assert rx.get("frameNumber")     == 2
    assert rx.get("command")         == 3
    assert rx.get("valueHB")         == 4
    assert rx.get("valueLB")         == 5
    assert rx.get("crc")             == 6

def test_wrongDataStream():
    with pytest.raises(ValueError):
        RX(0xfffffffff)


test_builds()
test_wrongDataStream()