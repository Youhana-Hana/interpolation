import sys
import os
import filecmp

sys.path.append('./lib')
import unittest
from lib import Program, FileTransport, Parser, Interpolator

class Test_Program(unittest.TestCase):
    def test_run(self):
            program = Program()
            inputFileName = os.path.join(os.getcwd(), 'integration/example_data/input_test_data.csv')
            outputFileName = os.path.join(os.getcwd(), 'integration/example_data/interpolated_data.csv')
            expectedFileName = os.path.join(os.getcwd(), 'integration/example_data/interpolated_test_data.csv')
            program.transport = FileTransport(inputFileName, outputFileName)
            program.parser = Parser()
            program.interpolator = Interpolator()

            program.run()

            self.assertTrue(filecmp.cmp(expectedFileName, outputFileName))

            
if __name__ == '__main__':
    unittest.main()
