#!/usr/bin/python
import sys, getopt, subprocess

def printHelp():
    print('./runner.py test: to run all tests')
    print('./runner.py coverage: to check coverage')
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hr:")
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            printHelp()
            sys.exit(0)
        elif opt == '-r':
            action = arg
            if action == 'test':
                subprocess.run('python -m unittest discover -v test', shell=True, check=True)
            elif action == 'coverage':
                completedProcess = subprocess.run('python -m coverage erase && python -m coverage run --source=lib -m unittest discover -v ./test && python -m coverage report --fail-under=100', shell=True)
                if completedProcess.returncode != 0:
                    print ('\n OPS! Coverage not met :(\n')
                else:
                    print('\n Well done :)')
                sys.exit(completedProcess.returncode)


if __name__ == '__main__':
    main(sys.argv[1:])
