
import unittest
from pathlib import Path
import day2

class TestAdventDay2(unittest.TestCase):
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

    def test_day2_part2_brute_force(self):
        checklist = [((Path("./day2_input.txt").read_text(),5098658), (12, 2))]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day2.part2_brute_force(check[0][0], check[0][1]),check[1])

    def test_day2_part2_combine(self):
        checklist = [((12, 2), 1202)]
        for check in checklist:
            with self.subTest(check=check):
                self.assertEqual(day2.part2_combine(check[0]), check[1])


if __name__ == '__main__':
    unittest.main()