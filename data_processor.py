import numpy as np
import pandas as pd
import random


def get_random_matrix(num_rows, num_cols):
    matrix = np.random.uniform( low = 0.0,
                               high = 1.0,
                               size = (num_rows,num_cols))
    return matrix
def get_file_dimensions(file_name):
    df = pd.read_csv(file_name,
                    sep = ",",
                    header=False)
    df.size(num_rows, num_cols)
    return (0,0)
def write_matrix_to_file(num_rows, num_columns, file_name):
    matrix = np.random.uniform(low = 0.0,
                       high = 1.0,
                       size = (num_rows, num_cols))
    fn = pd.DataFrame(file_name)
    fn.to_csv(new_file_name.csv)
    return new_file_name