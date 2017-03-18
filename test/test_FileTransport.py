import sys
sys.path.append('./lib')
import unittest
import mock
from lib import FileTransport
from StringIO import StringIO

class TestInputTransport(unittest.TestCase):
    def test_construct(self):
        transport = FileTransport('input', 'output')
        self.assertIsNotNone(transport)
        self.assertEqual('input', transport.inputFileName)
        self.assertEqual('output', transport.outputFileName)

    @mock.patch("__builtin__.open", create=True)
    def test_read(self, mock_open):
        mock_open.side_effect = [
            mock.mock_open(read_data='1,2,3\n4,5,6\n7,8,9\n').return_value,
        ]
        expected = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        transport = FileTransport('input', 'output')
        
        actual = transport.read()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
