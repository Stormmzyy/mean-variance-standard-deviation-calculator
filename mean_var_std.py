import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    def stats(func):
        return [
            func(matrix, axis=0).tolist(),  # down each column
            func(matrix, axis=1).tolist(),  # across each row
            func(matrix).tolist(),          # whole matrix flattened
        ]

    calculations = {
        'mean': stats(np.mean),
        'variance': stats(np.var),
        'standard deviation': stats(np.std),
        'max': stats(np.max),
        'min': stats(np.min),
        'sum': stats(np.sum),
    }

    return calculations