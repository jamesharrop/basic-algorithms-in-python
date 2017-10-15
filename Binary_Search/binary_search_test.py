import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.verbose = False 
        # ^ whether to print interim output to console during binary_search

    def test_simple_for_binary_search(self):
        input_list = [0, 1, 2, 3, 4, 5]
        self.assertTrue(binary_search(input_list, 1, self.verbose) == 1)

    def test_binary_search_with_a_list_of_6_ints(self):
        input_list = [1, 20, 3, 5, 7, 0]
        input_list.sort()

        for n in range(0, len(input_list)):
            output = binary_search(input_list, input_list[n], self.verbose)
            self.assertTrue(output == n)

    def test_binary_search_with_a_list_of_7_ints(self):
        input_list = [1, 20, 3, 5, 7, 0, 21]
        input_list.sort()

        for n in range(0, len(input_list)):
            output = binary_search(input_list, input_list[n], self.verbose)
            self.assertTrue(output == n)

    def test_binary_search_with_target_value_not_in_list(self):
        input_list = [1, 20, 3, 5, 7, 0, 21]
        input_list.sort()

        output = binary_search(input_list, 25, self.verbose)
        self.assertTrue(output == None)

    def test_binary_search_with_empty_list(self):
        input_list = []
        self.assertRaises(IndexError, lambda: binary_search(input_list, 1,
            self.verbose))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearch)
unittest.TextTestRunner(verbosity=2).run(suite)