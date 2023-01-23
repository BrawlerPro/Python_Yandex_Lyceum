from random import shuffle
from copy import deepcopy
from pprint import pprint


def make_assumptions(sudoku):
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if not value:
                values = set(row) \
                         | set([sudoku[k][j] for k in range(9)]) \
                         | set([sudoku[m][n] for m in range((i // 3) * 3, (i // 3) * 3 + 3)
                                for n in range((j // 3) * 3, (j // 3) * 3 + 3)])
                yield i, j, list(set(range(1, 10)) - values)


def solve_sudoku(matrix):
    if all([k for row in matrix for k in row]):
        return matrix
    assumptions = list(make_assumptions(matrix))
    shuffle(assumptions)

    x, y, values = min(assumptions, key=lambda x: len(x[2]))

    for v in values:
        new_sudoku = deepcopy(matrix)
        new_sudoku[x][y] = v
        s = solve_sudoku(new_sudoku)
        if s:
            return s
    return None



matrix = []

for i in range(4):
    nums = input()
    matr = []

    for i in range(0, 4):
        matr.append(nums[i])
    matrix.append(matr)

pprint(solve_sudoku(matrix))
