from Transport import Transport

class InputTransport(Transport):
    def read(self):
        rows = input('Please insert rows number: ')
        try:
            rowsCount = int(rows)
        except ValueError:
            print('Invalid rows count')
            return None
        else:
            matrix = [[j for j in input().split(',')] for i in range(rowsCount)]
            return matrix

    def write(self, output):
        print(output)
