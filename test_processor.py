import unittest
import data_processor as dp
import random
import numpy as np
import os
import pandas as pd
import csv

class TestData(unittest.TestCase):
      
    @classmethod
    def setUpClass(cls):
        np.random.seed(7)
        cls.array= np.random.rand(1,6)
        
    @classmethod
    def tearDownClass(cls):
        cls.test_list= None
        cls.rand_list= None
#unittests

    def test_to_start(self):
        self.assertTrue(True)

    def test_matrix(self):
        #test for matrix
        np.random.seed(7)
        np.testing.assert_array_equal(dp.get_random_matrix(1, 6, 7), self.array)
        np.testing.assert_raises(AssertionError,
                                 np.testing.assert_array_equal,
                                 dp.get_random_matrix(1,7, 7),
                                 self.array)
    def test_file_demensions(self):
        df= pd.read_csv('iris.data',
                        sep = ",",
                        header = None)
        self.assertEqual(dp.get_file_dimensions('iris.data'), (150,5))  
    def test_matrix_to_file(self):
        np.random.seed(7)
        matrix_file= dp.write_matrix_to_file(6,
                                             9,
                                             'elephant.csv',
                                             7)
        matrix_file= dp.write_matrix_to_file(3,
                                             7,
                                             'cow.csv',
                                             7)
        matrix= dp.get_random_matrix(6,
                                     9,
                                     7)
        with open('test.csv', 'w', newline= '') as f:
            writer= csv.writer(f, delimiter= ',')
            for row in matrix:
                writer.writerow(row)
        self.assertEqual(dp.get_file_dimensions('elephant.csv'),
                         dp.get_file_dimensions('test.csv'))
        self.assertNotEqual(dp.get_file_dimensions('cow.csv'),
                            dp.get_file_dimensions('test.csv'))
        
if __name__ == '__main__':
    unittest.main()