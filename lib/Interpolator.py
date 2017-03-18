class Interpolator:
    """ Interpolate matrix and calculate average for all entries with nan value"""
    def interpolate(self,  matrix):
        result = []
        for row in range(0, len(matrix)):
            result.append([])
            rowLength = len(matrix[row])
            for col in range(0, rowLength):
                value = matrix[row][col];
                if value =='nan':
                    value = self.getAverage(matrix, row, col)
                result[row].append(value)
        return result

    def getAverage(self, matrix, row, col):
        neighbours = self.get_neighbours(matrix, row, col)
        return self.calculate_average(neighbours)

    def get_neighbours(self, matrix, row, col):
        matrixLength = len(matrix);
        rowLength = len(matrix[row])

        neighbours = []
        if(col > 0):
            value  = matrix[row][col -1]
            self.push_value(neighbours, value)

        if(col < rowLength - 1):
            value  = matrix[row][col + 1]
            self.push_value(neighbours, value)

        if(row > 0):
            value  = matrix[row - 1][col]
            self.push_value(neighbours, value)

        if(row < matrixLength - 1):
            value  = matrix[row + 1][col]
            self.push_value(neighbours, value)

        return neighbours

    def calculate_average(self, neighbours):
        total = sum(neighbours);
        count = len(neighbours);
        return round(float(total) / float (count), 6)

    def push_value(self, values, value):
        if(value != 'nan'):
            values.append(value)
