import unittest
from insertion_sort import insertion_sort
import random

class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort_with_a_small_list_of_ints(self):
        input_list = [1, 20, 3, 5, 7, 0]
        expected_list = [0, 1, 3, 5, 7, 20]
        self.assertTrue(insertion_sort(input_list) == expected_list)

    def test_insertion_sort_with_a_small_list_of_mixed_items(self):
        '''  '''
        input_list = [1.2, 20, "a", -5.23, 7, 0]
        self.assertRaises(TypeError, lambda: insertion_sort(input_list))

    def test_insertion_sort_with_a_random_list_of_ints(self):
        list_length = random.randrange(20,100)
        input_list = []
        for n in range(0, list_length):
            input_list.append(random.randrange(-1000,1000))
        self.assertTrue(insertion_sort(input_list) == sorted(input_list))

suite = unittest.TestLoader().loadTestsFromTestCase(TestInsertionSort)
unittest.TextTestRunner(verbosity=2).run(suite)
