class Parser:
    """ Parse string matrix and covert each entry to double value, skipping nan values"""
    def parse(self,  matrix):
        result = []
        for row in range(0, len(matrix)):
            result.append([])
            rowLength = len(matrix[row])
            for col in range(0, rowLength):
                value = matrix[row][col];
                if value !='nan':
                    value = float(value)
                result[row].append(value)
        return result
