import unittest
import day1

class TestAdvent(unittest.TestCase):
    def test_day1_module_fuel(self):
        checklist = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day1.module_fuel_required(check[0]), check[1])

    def test_day1_total_fuel(self):
        checklist = [12, 14, 1969]
        self.assertEqual(day1.total_fuel_required(checklist), 658)
    

if __name__ == '__main__':
    unittest.main()