from lib import InputTransport
from lib import Parser
from lib import Interpolator

class Program:
    def __init__(self):
        self.transport = InputTransport()
        self.parser = Parser()
        self.interpolator = Interpolator()

    def run(self):
        try:
            input = self.transport.read()
            parsed_input = self.parser.parse(input)
            result = self.interpolator.interpolate(parsed_input)
        except ValueError:
            self.transport.write('Invalid matrix!')
        else:
            self.transport.write(result)
