import unittest
import data_processor as dp
import random
import numpy as np
import os

class TestUtils(unittest.TestCase):
    test_list= [1,3,5,4,6,]
    
    @classmethod
    def setUpClass(cls):
        cls.test_list= [1,3,5,4,6,]
        cls.rand_list= []
        for i in range (15):
            rand_int= random.randint(0,14)
            cls.rand_list.append(rand_int)
            
    @classmethod
    def tearDownClass(cls):
        cls.test_list= None
        cls.rand_list= None
#unittests

    def test_to_start(self):
        self.assertTrue(True)
    
    def get_random_matrix(self):
        #test for matrix
        self.assertTrue(dp.get_random_matrix())
        
    def get_file_dimensions(self):

    def write_matrix_to_file(self):
        
        
if __name__ == '__main__':
    unittest.main()
