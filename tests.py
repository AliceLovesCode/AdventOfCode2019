import unittest
import day1
import day2

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

    def test_day2_opcode1(self):
        checklist = [("1,0,0,0,99","2,0,0,0,99"), ("1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50"),("2,3,0,3,99","2,3,0,6,99"),("2,4,4,5,99,0","2,4,4,5,99,9801"),("1,1,1,4,99,5,6,0,99","30,1,1,4,2,5,6,0,99")]
        for check in checklist:
            with self.subTest(check=check):
                program_run = day2.ProgramRun(check[0])
                program_run.run()
                self.assertEqual(str(program_run), check[1])

    def test_day2_parse(self):
        checklist = [("1,0,0,0,99",[1,0,0,0,99])]
        for check in checklist:
            with self.subTest(check=check):
                program_run = day2.ProgramRun(check[0])
                self.assertEqual(program_run.program, check[1])


if __name__ == '__main__':
    unittest.main()