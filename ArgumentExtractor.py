import sys

# a class to extract arguments to a dictionary and check arguments
class ArgumentExtractor:
    def __init__(self, args):
        self.args = args

    def extract(self):
        argsMap = {}
        for i in range(0, len(self.args), 2):
            if (self.args[i].startswith('-')):
                argsMap[self.args[i]] = self.args[i + 1]

        self.argsMap = argsMap
        return argsMap

    def checkArgs(self):
        if (len(self.args) < 2):
            print('''Usage:  python Main.py -ip [IP] -p [PORT] -proto [PROTOCOL]\n
            IP: a single ipv4 address or range of ipv4 addresses(Eg. 127.0.0.1-255)
            PORT: a single port number, range of port numbers(Eg. 1-1023), or list of port numbers separated by comma(Eg. 80,443)
            PROTOCOL: either tcp or udp\n''')
            sys.exit()
        
        if ('-ip' not in self.argsMap):
            print("No ipv4 address to scan! Please specify ipv4 address with flag -ip")
            sys.exit()

        if ('-p' not in self.argsMap):
            print("No port number(s) to scan! Please specify port number with flag -p")
            sys.exit()

        if ('-proto' not in self.argsMap):
            print("No protocol for scan! Please specify protocol with flag -proto")
            sys.exit()
