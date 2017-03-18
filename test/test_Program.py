import sys
sys.path.append('./lib')
import unittest
import mock
import math
from Program import Program
from Transport import Transport
from Parser import Parser
from Interpolator import Interpolator

class Test_Program(unittest.TestCase):
    def test_construct(self):
        program = Program()
        self.assertIsNotNone(program)

    def test_run(self):
            program = Program()
            program.transport = mock.create_autospec(Transport)
            program.parser = mock.create_autospec(Parser)
            program.interpolator = mock.create_autospec(Interpolator)

            program.transport.read.return_value = 'input'
            program.parser.parse.return_value = 'parsed_input'
            program.interpolator.interpolate.return_value = 'output'


            actual = program.run()

            program.transport.read.assert_called()
            program.parser.parse.assert_called()
            program.parser.parse.assert_called_with('input')
            program.interpolator.interpolate.assert_called_with('parsed_input')
            program.transport.write.assert_called_with('output')
    
    def test_run_invalid_input(self):
            program = Program()
            program.transport = mock.create_autospec(Transport)
            program.parser = mock.create_autospec(Parser)
            program.interpolator = mock.create_autospec(Interpolator)

            program.transport.read.return_value = 'input'
            program.parser.parse.side_effect = ValueError('Error')
            program.interpolator.interpolate.return_value = 'output'


            actual = program.run()

            program.transport.read.assert_called()
            program.parser.parse.assert_called()
            program.parser.parse.assert_called_with('input')
            program.interpolator.interpolate.assert_not_called()
            program.transport.write.assert_called_with('Invalid matrix!')
            
if __name__ == '__main__':
    unittest.main()
