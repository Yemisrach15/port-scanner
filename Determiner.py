import sys
from PortScanner import PortScanner
from TimeCounter import TimeCounter

# a class to determine single/multiple ip addresses, single/multiple ports
class Determiner:
    def __init__(self, ip, ports, proto):
        self.ip = ip
        self.ports = ports
        self.proto = proto

    def isSingleIp(self):
        return '-' not in self.ip

    def isSinglePort(self):
        return self.ports.isnumeric()

    def scan(self):
        if (self.isSingleIp()):
            self.scanSingleIp(self.ip)
        else:
            self.scanMultipleIp()

    def scanSingleIp(self, ip):
        scanner = PortScanner(ip, self.proto)
        self.formatPrint(scanner.target)
        self.constructPortList()
        scanner.scanList(self.portList)

    def scanMultipleIp(self):
        ipBase = (self.ip.split('-')[0]).split('.')[0:-1]
        ipRangeI = int((self.ip.split('-')[0]).split('.')[-1])
        ipRangeF = int(self.ip.split('-')[1])

        timeCounter = TimeCounter()
        timeCounter.start()
        for ip4 in range(ipRangeI, ipRangeF):
            self.scanSingleIp("{}.{}.{}.{}".format(*ipBase, ip4))
        timeCounter.stop()
        self.formatTotalTime(ipRangeI, ipRangeF, timeCounter.total())

    def constructPortList(self):
        if (self.isSinglePort()):
            self.portList = [int(self.ports)]
        elif ('-' in self.ports):
            portInitial = int(self.ports.split('-')[0])
            portEnd = int(self.ports.split('-')[1])
            self.portList = list(range(portInitial, portEnd))
        elif (',' in self.ports):
            self.portList = [int(i, base=10) for i in self.ports.split(',')]
        else:
            sys.exit()

    def formatPrint(self, target):
        if (not self.isSingleIp()):
            print("=" * 50)

        print("-" * 50)
        print("Scanning Target: " + target)
        print("-" * 50)

    def formatTotalTime(self, ipRangeI, ipRangeF, totalTime):
        print("=" * 50)
        print("Total scanning time for {} ipv4 addresses: {}".format((ipRangeF - ipRangeI), totalTime))
