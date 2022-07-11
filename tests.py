import unittest
import floyd


class FloydTests(unittest.TestCase):

    def test_imperative(self):
        import sys
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(floyd.floyd(graph),
                         [[0, 7, 12, 8], [NO_PATH, 0, 5, 7], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]])

    def test_recursive(self):
        import sys
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(floyd.floyd_recursion(floyd.graph),
                         [['1 1 => (0)', '1 2 => (7)', '1 3 => (12)', '1 4 => (8)'],
                          ['2 no path to 1 => (9223372036854775807)', '2 2 => (0)', '2 3 => (5)', '2 4 => (7)'],
                          ['3 no path to 1 => (9223372036854775807)', '3 no path to 2 => (9223372036854775807)',
                           '3 3 => (0)', '3 4 => (2)'],
                          ['4 no path to 1 => (9223372036854775807)', '4 no path to 2 => (9223372036854775807)',
                           '4 no path to 3 => (9223372036854775807)', '4 4 => (0)']])


if __name__ == '__main__':
    unittest.main()
