import sys
sys.path.append('../lib')
import unittest
import mock
from lib import Transport

class TestTransport(unittest.TestCase):
    def test_construct(self):
        transport = Transport()
        self.assertIsNotNone(transport)

    def test_read(self):
        with mock.patch('__builtin__.input', side_effect = ['3', '1,2,3', '4,5,6', '7,8,9']):
            expected = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            transport = Transport()

            actual = transport.read()

            self.assertEqual(expected, actual)


    def test_read_with_non_values(self):
        with mock.patch('__builtin__.input', side_effect = ['5', '37.454012,95.071431,73.199394,59.865848,nan', '15.599452,5.808361,86.617615,60.111501,70.807258', '2.058449,96.990985,nan,21.233911,18.182497', 'nan,30.424224,52.475643,43.194502,29.122914', '61.185289,13.949386,29.214465,nan,45.606998' ]):
            expected = [['37.454012', '95.071431', '73.199394', '59.865848' , 'nan'], ['15.599452', '5.808361', '86.617615', '60.111501', '70.807258'], ['2.058449', '96.990985', 'nan', '21.233911', '18.182497'], ['nan', '30.424224', '52.475643', '43.194502', '29.122914'], ['61.185289', '13.949386', '29.214465', 'nan', '45.606998']]
 
            transport = Transport()

            actual = transport.read()

            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
