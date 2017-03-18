import sys
sys.path.append('./lib')
import unittest
import mock
import math
from lib import Parser

class Test_Parser(unittest.TestCase):
    def test_construct(self):
        parser = Parser()
        self.assertIsNotNone(parser)

    def test_read_with_nan_values(self):
            input = [['37.454012', '95.071431', '73.199394', '59.865848' , 'nan'], ['15.599452', '5.808361', '86.617615', '60.111501', '70.807258'], ['2.058449', '96.990985', 'nan', '21.233911', '18.182497'], ['nan', '30.424224', '52.475643', '43.194502', '29.122914'], ['61.185289', '13.949386', '29.214465', 'nan', '45.606998']]
            expected = [[37.454012, 95.071431, 73.199394, 59.865848 , 'nan'], [15.599452, 5.808361, 86.617615, 60.111501, 70.807258], [2.058449, 96.990985, 'nan', 21.233911, 18.182497], ['nan', 30.424224, 52.475643, 43.194502, 29.122914], [61.185289, 13.949386, 29.214465, 'nan', 45.606998]]
            parser = Parser()
            
            actual = parser.parse(input)

            self.assertEqual(expected, actual)
    
if __name__ == '__main__':
    unittest.main()
