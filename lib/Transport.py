import abc

class Transport():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self, output):
        pass
