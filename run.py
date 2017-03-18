#!/usr/bin/python
import sys
sys.path.append('./lib')
from lib import Program

def main(argv):
    program = Program()
    program.run()

if __name__ == '__main__':
    main(sys.argv[1:])
