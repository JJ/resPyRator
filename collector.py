from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server
import sys
import glob
import fakeSerial
from reader import *

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class ReespiratorCollector(object):
    def collect(self):
        c = GaugeMetricFamily('reespirator', 'Reespirator', labels=['vars'])
        # TODO: Read real values from serial port
        c.add_metric(['rpm'], 12)
        c.add_metric(['peakPressure'], 28)
        c.add_metric(['peepPressure'], 6)
        c.add_metric(['flow'], 3)
        c.add_metric(['battery'], 60)
        yield c

REGISTRY.register(ReespiratorCollector())



if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8001)

    print("Prueba")
    available_ports = serial_ports()
    print(available_ports)
    s = serial.Serial(port=available_ports[0], baudrate=115200, timeout=0.1)
    counter = 0

    while True:

        packet = recv_packet_blocking(s)
        print_packet(packet)
        if check_crc(packet):
            print("Packet received correctly")
        else:
            print("WRONG PACKET!!")
        packet.Header = 12
        generate_crc(packet)
        print("Sending packet with crc:%d" % packet.Crc)
        send_packet(s,packet)
        #print("New Packet received[%d]" % counter)
        #time.sleep(0.5)
        #send_packet(s,p)
        counter = counter +1


        pass
