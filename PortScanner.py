import socket
import sys

class PortScanner:
    def __init__(self, ip, proto):
        try:
            self.target = socket.gethostbyname(ip)
        except socket.gaierror:
            print("\nHost name could not be resolved")
            sys.exit()

        self.protoString = proto
        if (proto == "tcp"):
            self.proto = socket.SOCK_STREAM
        elif (proto == "udp"):
            self.proto = socket.SOCK_DGRAM

    def scanRange(self, pi, pf):
        try:
            print("PORT\tPROTOCOL\tSERVICE")
            openPorts = 0
            for port in range(pi, pf):
                s = socket.socket(socket.AF_INET, self.proto)
                socket.setdefaulttimeout(1)

                result = s.connect_ex((self.target, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port, self.protoString)
                        openPorts += 1
                        print("{}\t{}\t\t{}".format(port, self.protoString, service))
                    except OSError:
                        pass
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
            print("PORT\tPROTOCOL\tSERVICE")
            openPorts = 0
            for port in portsList:
                s = socket.socket(socket.AF_INET, self.proto)
                socket.setdefaulttimeout(1)

                result = s.connect_ex((self.target, port))
                if result == 0:     
                    try:
                        service = socket.getservbyport(port, self.protoString)
                        openPorts += 1
                        print("{}\t{}\t\t{}".format(port, self.protoString, service))
                    except OSError:
                        pass
                s.close()
                
            print("\nFinished Scanning: {} of {} scanned ports open".format(openPorts, len(portsList)))
        except KeyboardInterrupt:
            print("\nCancelled Scanning...")
            sys.exit()
        except socket.error:
            print("\nServer not responding")
            sys.exit()