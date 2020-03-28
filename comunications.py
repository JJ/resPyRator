from enum import Enum

class CommunicationFrame:
    _dataFrame

class RX(CommunicationFrame): 
    class Address(Enum):
        header                   = "0x00"
        protocolVersion          = "0x01"
        frameNumber              = "0x02"
        command                  = "0x03"
        valueHB                  = "0x04" # High byte
        valueLB                  = "0x05" # Low byte
        crc                      = "0x06"

    class Command(Enum):
        setRPM                   = "0x01"
        setPeakPressure          = "0x02"
        setPeepPressure          = "0x03"
        setTriggerFlow           = "0x04"
        setRamp                  = "0x05"
        setAlarmVolumeLow        = "0x11"
        setAlarmVolumeHigh       = "0x12"
        setAlarmRPMLow           = "0x13"
        setAlarmRPMHigh          = "0x14"
        setAlarmPeakPressureLow  = "0x15"
        setAlarmPeakPressureHigh = "0x16"
        setAlarmPeepPressureLow  = "0x17"
        setAlarmPeepPressureHigh = "0x18"
        setAlarmBatteryLow       = "0x19"
        getAlarmVolumeLow        = "0x21"
        getAlarmVolumeHigh       = "0x22"
        getAlarmRPMLow           = "0x23"
        getAlarmRPMHigh          = "0x24"
        getAlarmPeakPressureLow  = "0x25"
        getAlarmPeakPressureHigh = "0x26"
        getAlarmPeepPressureLow  = "0x27"
        getAlarmPeepPressureHigh = "0x28"
        getAlarmBatteryLow       = "0x29"
        getFimwareVersion        = "0x50"

    def __init__(self):
        self._dataFrame = list(7)    

    def get(self, address):
        return self._dataFrame[int (address)]

class TX(CommunicationFrame):
    class Address(Enum):
        Header 0x00
        protocolVersion 0x01
        UUID 0x02
        Tag/Free use SN 0x06
        RPMsetting 0x0A
        RPMsetting 0x0B
        RPM measure 0x0C
        RPM measure 0x0D
        PeakPressureSetting 0x0E
        PeakPressureSetting 0x0F
        PeakPressure measure 0x10
        PeakPressure measure 0x11
        PeepPressure setting 0x12
        PeepPressure setting 0x13
        PeepPressure measure 0x14
        PeepPressure measure 0x15
        TriggerFlow setting 0x16
        TriggerFlow setting 0x17
        Flow measure 0x18
        Flow measure 0x19
        Ramp setting 0x1A
        Ramp setting 0x1B
        ActiveAlarmCode 0x1C
        Status Bit Field 0x1D
        tempValueEnc1 0x1E
        tempValueEnc2 0x1F
        tempValueEnc3 0x20
        tempValueEnc4 0x21
        Answer (high) 0x22
        Answer (low) 0x23
        Answer to Frame Number 0x24
        CRC 0x25


    def __init__(self):
        self._dataFrame = list(15)    