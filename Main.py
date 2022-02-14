from TimeCounter import *
from PortScanner import *
import sys

timeCounter = TimeCounter()

# check command line arguments
if (len(sys.argv) < 2):
    print('''Usage:  python Main.py -ip [IP] -p [PORT] -proto [PROTOCOL]\n
IP: a single ipv4 address or range of ipv4 addresses(Eg. 127.0.0.1-255)
PORT: a single port number, range of port numbers(Eg. 1-1023), or list of port numbers separated by comma(Eg. 80,443)
PROTOCOL: either tcp or udp''')
    sys.exit()

if ("-ip" in sys.argv):
    ip = sys.argv[sys.argv.index("-ip") + 1]
else:
    print("No ipv4 address to scan! Please specify ipv4 address with flag -ip")
    sys.exit()

if ("-p" in sys.argv):
    ports = sys.argv[sys.argv.index("-p") + 1]
else:
    print("No port number(s) to scan! Please specify port number with flag -p")
    sys.exit()

if ("-proto" in sys.argv):
    proto = sys.argv[sys.argv.index("-proto") + 1]
else:
    print("No protocol for scan! Please specify protocol with flag -proto")
    sys.exit()


# function to determine if a single port or multiple ports are to be scanned and scans
def scanPorts(ports, scanner):
    if ('-' in ports):
        portInitial = int(ports.split('-')[0])
        portEnd = int(ports.split('-')[1])
        scanner.scanRange(portInitial, portEnd)

    elif (',' in ports):
        portList = [int(i, base=10) for i in ports.split(',')]
        scanner.scanList(portList)

    elif (ports.isnumeric()):
        portList = [int(ports)]
        scanner.scanList(portList)

# determine if ip is single or in range
if ('-' not in ip):
    tcpScan = PortScanner(ip, proto)
    print("-" * 50)
    print("Scanning Target: " + tcpScan.target)
    print("-" * 50)
    scanPorts(ports, tcpScan)

else:
    ipBase = (ip.split('-')[0]).split('.')[0:-1]
    ipRangeI = int((ip.split('-')[0]).split('.')[-1])
    ipRangeF = int(ip.split('-')[1])
    
    timeCounter = TimeCounter() # time counter for all ip address scans
    timeCounter.start()
    for ip4 in range(ipRangeI, ipRangeF): 
        tcpScan = PortScanner("{}.{}.{}.{}".format(*ipBase, ip4), proto)
        print("=" * 50)
        print("-" * 50)
        print("Scanning Target: " + tcpScan.target)
        print("-" * 50)
        scanPorts(ports, tcpScan)

    timeCounter.stop()
    print("=" * 50)
    print("Total scanning time for {} ipv4 addresses: {}".format((ipRangeF - ipRangeI), timeCounter.total()))
