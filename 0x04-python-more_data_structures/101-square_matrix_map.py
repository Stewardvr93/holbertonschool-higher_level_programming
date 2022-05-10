#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda pri: list(map(lambda seg: seg*seg, pri)), matrix))
