import socket
import sys

class TCPScan:
    def __init__(self, ip):
        try:
            self.target = socket.gethostbyname(ip)
        except socket.gaierror:
            print("\nHost name could not be resolved")
            sys.exit()

    def scanRange(self, pi, pf):
        try:
            print("PORT\tSERVICE")
            openPorts = 0
            for port in range(pi, pf):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                result = s.connect_ex((self.target, port))
                if result == 0:
                    openPorts += 1
                    service = socket.getservbyport(port)
                    print("{}\t{}".format(port, service))
                s.close()
                
            print("\nFinished Scanning: {} of {} scanned ports open".format(openPorts, (pf - pi)))
        except KeyboardInterrupt:
            print("\nCancelled Scanning...")
            sys.exit()
        except socket.error:
            print("\nServer not responding")
            sys.exit()

    def scanList(self, portsList):
        try:
            print("PORT\tSERVICE")
            openPorts = 0
            for port in portsList:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                socket.setdefaulttimeout(1)

                result = s.connect_ex((self.target, port))
                if result == 0:
                    openPorts += 1
                    service = socket.getservbyport(port)
                    print("{}\t{}".format(port, service))
                s.close()
                
            print("\nFinished Scanning: {} of {} scanned ports open".format(openPorts, len(portsList)))
        except KeyboardInterrupt:
            print("\nCancelled Scanning...")
            sys.exit()
        except socket.error:
            print("\nServer not responding")
            sys.exit()