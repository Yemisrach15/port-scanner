from TimeCounter import *
from PortScanner import *
import sys

timeCounter = TimeCounter()

ip = sys.argv[2]
ports = sys.argv[4]
proto = sys.argv[6]

# determine if ip is single or in range
if ('-' not in ip):
    tcpScan = PortScanner(ip, proto)
    print("-" * 50)
    print("Scanning Target: " + tcpScan.target)
    print("-" * 50)
    # determine if single or multiple ports
    if ('-' in ports):
        portInitial = int(ports.split('-')[0])
        portEnd = int(ports.split('-')[1])

        timeCounter.start()
        tcpScan.scanRange(portInitial, portEnd)   
        timeCounter.stop()

        print("Total scanning time: " + timeCounter.total())
    elif (',' in ports):
        portList = [int(i, base=10) for i in ports.split(',')]
        
        timeCounter.start()
        tcpScan.scanList(portList)   
        timeCounter.stop()

        print("Total scanning time: " + timeCounter.total())
    elif (ports.isnumeric()):
        portList = [int(ports)]

        timeCounter.start()
        tcpScan.scanList(portList)   
        timeCounter.stop()

        print("Total scanning time: " + timeCounter.total())

else:
    ipBase = (ip.split('-')[0]).split('.')[0:-1]
    ipRangeI = int((ip.split('-')[0]).split('.')[-1])
    ipRangeF = int(ip.split('-')[1])
    
    
    timeCounter = TimeCounter()
    timeCounter.start()
    for ip4 in range(ipRangeI, ipRangeF): 
        tcpScan = PortScanner("{}.{}.{}.{}".format(*ipBase, ip4), proto)
        print("=" * 50)
        print("-" * 50)
        print("Scanning Target: " + tcpScan.target)
        print("-" * 50)
        # determine if single or multiple ports
        if ('-' in ports):
            portInitial = int(ports.split('-')[0])
            portEnd = int(ports.split('-')[1])
            tcpScan.scanRange(portInitial, portEnd)

        elif (',' in ports):
            portList = [int(i, base=10) for i in ports.split(',')]
            tcpScan.scanList(portList)

        elif (ports.isnumeric()):
            portList = [int(ports)]
            tcpScan.scanList(portList)

    print("\n" + "="*50)
    timeCounter.stop()
    print("Total scanning time: " + timeCounter.total())
