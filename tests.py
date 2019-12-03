import unittest
import day1

class TestAdvent(unittest.TestCase):
    def test_day1_module_fuel(self):
        checklist = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day1.mass_fuel_required(check[0]), check[1])

    def test_day1_total_fuel(self):
        checklist = [12, 14, 1969]
        self.assertEqual(day1.part1_summed_fuel_required(checklist), 658)
    
    def test_day1_recursive_fuel(self):
        checklist = [(1969, 966), (100756, 50346)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day1.recursive_fuel_required(check[0]), check[1])
        

if __name__ == '__main__':
    unittest.main()