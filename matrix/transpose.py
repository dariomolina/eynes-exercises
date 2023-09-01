import pandas as pd


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
    df = pd.DataFrame(matrix)
    transposed_df = df.transpose()
    transposed_matrix = transposed_df.values.tolist()
    return transposed_matrix
