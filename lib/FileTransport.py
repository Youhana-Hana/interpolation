import os
from lib import Transport

class FileTransport(Transport):
    def __init__(self, fileName, outputFileName):
        self.inputFileName = fileName
        self.outputFileName = outputFileName
        pass

    def read(self):
        try:
            with open(self.inputFileName, 'r') as f:
                lines = f.readlines()
        except OSError:
            return None
        else:
            matrix = [[j for j in line.strip('\n').split(',')] for line in lines]
            return matrix

    def write(self, output):
        with open(self.outputFileName, 'w') as f:
            for line in output:
                f.write(','.join(str(item) for item in line))
                f.write('\n')
