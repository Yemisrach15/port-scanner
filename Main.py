from ArgumentExtractor import ArgumentExtractor
from Determiner import Determiner
import sys

def main(argv):
    argumentExtractor = ArgumentExtractor(argv)
    args = argumentExtractor.extract()
    argumentExtractor.checkArgs()

    determiner = Determiner(args['-ip'], args['-p'], args['-proto'])
    determiner.scan()

if __name__ == "__main__":
    main(sys.argv[1:])
    