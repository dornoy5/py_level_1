from typing import List

def matrix_sum(matrix: List[list[int]])-> int:
    return sum(sum(row) for row in matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix sum:", matrix_sum(matrix))