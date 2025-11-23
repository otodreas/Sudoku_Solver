import numpy as np

class Sudoku:
    def __init__(self, size):
        self.size = size

    def create_matrix(self):
        m = np.zeros(81)
        values = np.random.randint(0, 8, self.size)
        positions = np.array(range(0, 81))
        values_positions = np.random.choice(positions, self.size, False)
        m[values_positions] = values
        m = np.reshape(m, (9, 3, 3))
        self.matrix = m

    def is_valid(self):
        for i in range(9):
            sub_m = self.matrix[i]
            row = self.matrix[i]
            num_freqs = np.unique(sub_m, return_counts=True)[1][1:]
            if np.sum(num_freqs) > len(num_freqs):
                return False

        return True