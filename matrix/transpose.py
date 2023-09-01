
def transpose(matrix):
    """
    Transpose a given matrix.
    This function takes a 2D array of integers as
    input and returns its transposed matrix.
    The transposed matrix is obtained by exchanging
    rows and columns of the original matrix.
    Args:
        matrix (list[list[int]]): The input matrix to be transposed.
    Returns:
        list[list[int]]: The transposed matrix.
    """
    len_cols = len(matrix[0])
    len_rows = len(matrix)
    transpose_matrix = [[0] * len_rows for _ in range(len_cols)]
    for i, array in enumerate(range(len_rows)):
        for j, value in enumerate(range(len_cols)):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix
