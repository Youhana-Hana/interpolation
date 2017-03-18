from Transport import Transport
from Parser import Parser
from Interpolator import Interpolator

class Program:
    def __init_(self):
        self.transport = Transport()
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
