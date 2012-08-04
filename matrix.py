
# ~ encoding: utf-8 ~

class Matrix(object):
    """
    """
    
    def __init__(self, matrix_input):
        """
        """
        self.values = matrix_input
        
    def get_row(self, row):
        """
        """
        return self.values[row]

    def get_col(self, col):
        """
        """
        return [row[col] for row in self.values ]
    
    def set_value(self, row, col, value):
        """
        """
        self.values[row][col] = value
    
    def get_value(self, row, col):
        """
        """
        return self.values[row][col]

    def get_row_count(self):
        """
        """
        return len(self.values)

    def get_col_count(self):
        """
        """
        return len(self.values[0])
    
    def get_values(self):
        """
        """
        return self.values

    def __repr__(self):
        """
        """
        matrix_string = ""
        x = 0
        for row in self.values:
            if x == 0:
                matrix_string += "%s" % (str(row))
                x = 1
            else:
                matrix_string += "\n%s" % (str(row))
        return matrix_string