import numpy as np
import pandas as pd
import random


def get_random_matrix(num_rows,
                      num_cols,
                      seed):
    np.random.seed(seed)
    matrix = np.random.uniform( low = 0.0,
                               high = 1.0,
                               size = (num_rows,num_cols))
    return matrix
def get_file_dimensions(file_name):
    df = pd.read_csv(file_name,
                    sep = ",",
                    header= None)
    file_dim=df.shape
    return file_dim
def write_matrix_to_file(num_rows,
                         num_cols,
                         file_name,
                         seed):
    np.random.seed(seed)
    matrix= get_random_matrix(num_rows,
                              num_cols,
                              seed)
    matrix_file = np.savetxt(file_name,
                            matrix,
                            delimiter= ',')
    
    return matrix_file

if __name__ == '__main__':
    main()