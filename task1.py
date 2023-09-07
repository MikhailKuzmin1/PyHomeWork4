# Напишите функцию транспонирования матрицы.


def matrix_transp(matrix: list) -> list:
    zip_matrix = zip(*matrix)
    return [list(i) for i in zip_matrix]


print(matrix_transp([[1,2,3],[4,5,6]]))

