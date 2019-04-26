from final_project import *
import unittest
import csv
import random
import itertools

# testing intial data set
class PartOne(unittest.TestCase):
    def test_movies_clean(self): ## Testing the csv file with movie data
        self.cleaned_file = open('movies_clean.csv','r', encoding = 'utf-8')
        self.row_reader = self.cleaned_file.readlines()
        # print(self.row_reader) # For debug
        self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Title / first value in the row at index 1")
        self.assertTrue(self.row_reader[20].split(",")[0], "Testing that there is a Title / first value in the row at index 20")
        self.cleaned_file.close()

# testing instances
class PartThree(unittest.TestCase):
    def setUp(self):
        self.movie_instance = Movie()
        self.director_instance = Director()
        self.rating_instance = Ratings()

    def test_instances(self):
        self.assertIsInstance(self.movie_instance, Movie, "testing if instance is of class Movie")
        self.assertIsInstance(self.director_instance, Director, "testing if instance is of class Director")
        self.assertIsInstance(self.rating_instance, Ratings, "testing if instance is of class Ratings")

# testing values of class instance attributes
class PartTwo(unittest.TestCase):
    def setUp(self):
        self.movie_instance = Movie(title = "Legendary")
        self.director_instance = Director(name = "John Wick")
        self.rating_instance = Ratings(imdb_rating = 6)

    def test_instances(self):
        self.assertEqual(self.movie_instance.title, "Legendary", "Testing that the instance of Movie has the correct title value")
        self.assertEqual(self.director_instance.name, "John Wick", "Testing that the instance of director has the correct name value")
        self.assertEqual(self.rating_instance.imdb_rating, 6, "Testing that the instance of Rating has the correct imdb rating value")

if __name__ == "__main__":
    unittest.main(verbosity=2)
