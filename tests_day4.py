
import unittest
import day4

class TestAdventDay4(unittest.TestCase):
    def test_meets_criteria_part1(self):
        checklist = [(111111, True), (223450, False), (123789, False), (11, False), (643603, False), (123444, True), (112233, True), (111122, True)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day4.meets_criteria_part1(check[0]), check[1])

    def test_valid_values_within_range_part1(self):
        checklist = [((1,100), 0), ((0, 99999), 0), ((0, 111112), 1)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day4.valid_values_in_range_part1(check[0][0], check[0][1]), check[1])

    def test_meets_criteria_part2(self):
        checklist = [(111111, False), (223450, False), (123789, False), (11, False), (643603, False), (123444, False), (112233, True), (111122, True)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day4.meets_criteria_part2(check[0]), check[1])

    def test_valid_values_within_range_part2(self):
        checklist = [((1,100), 0), ((0, 99999), 0), ((0, 111112), 0)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day4.valid_values_in_range_part2(check[0][0], check[0][1]), check[1])

if __name__ == '__main__':
    unittest.main()