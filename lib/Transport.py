class Transport:
    def read(self):
        rows = input('Please insert rows number: ')
        rowsCount = int(rows)
        matrix = [[j for j in input().split(',')] for i in range(rowsCount)]
        return matrix
