import unittest
import day3

class TestAdventDay3(unittest.TestCase):
    def test_manhattan_distance(self):
        checklist = [(((0,0),(1,0)), 1),(((1,0),(0,0)), 1), (((20,0),(0,0)), 20), (((20,0),(0,20)), 40)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day3.manhattan_distance(check[0][0], check[0][1]), check[1])

if __name__ == '__main__':
    unittest.main()