from final_project import *
import unittest
import csv
import random
import itertools

class PartOne(unittest.TestCase):
    def test_movies_clean(self): ## Testing the csv file with movie data
        self.cleaned_file = open('movies_clean.csv','r', encoding = 'utf-8')
        self.row_reader = self.cleaned_file.readlines()
        # print(self.row_reader) # For debug
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Title / first value in the row at index 1")
        self.assertTrue(self.row_reader[20].split(",")[0], "Testing that there is a Title / first value in the row at index 20")
        self.cleaned_file.close()

class PartTwo(unittest.TestCase):
    def test_csv_data_stored(self):
        


if __name__ == "__main__":
    unittest.main(verbosity=2)
