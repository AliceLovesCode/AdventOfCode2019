import sys
from pathlib import Path
program_step = 4

def opcode(code, operand1, operand2):
    if code == 1:
        return operand1 + operand2
    elif code == 2:
        return operand1 * operand2

def both_parts():
    starting_program_input = Path(sys.argv[1]).read_text()
    program_run = TwoInputProgramRun(starting_program_input, 12, 2)
    program_run.run()
    print(str(program_run.output()))

    result = part2_brute_force(starting_program_input, 19690720)
    print(str(part2_combine(result)))

def part2_brute_force(program_text, target_value):
    i = 0
    j = 0
    for i in range (0, 99):
        for j in range (0, 99):
            program_run = TwoInputProgramRun(program_text, i, j)
            program_run.run()
            if (program_run.output() == target_value):
                return (i, j)

def part2_combine(tuple):
    return (100 * tuple[0]) + tuple[1]

class ProgramRun:
    program_counter = 0
    program = []
    program_finished = False

    def __init__(self, program_string):
        self.load_program(program_string)

    def __str__(self):
        return ','.join(str(x) for x in self.program)

    def load_program(self, program_string):
        self.program = [int(x) for x in program_string.split(",")]

    def step(self):
        if self.program[self.program_counter] == 99:
            self.program_finished = True
            return
        self.program[self.program[self.program_counter+3]] = opcode(self.program[self.program_counter], self.load_operand(self.program[self.program_counter+1]), self.load_operand(self.program[self.program_counter+2]))
        self.program_counter += program_step

    def load_operand(self, address):
        return self.program[address]

    def run(self):
        while not self.program_finished:
            self.step()
    def output(self):
        return self.program[0]

class TwoInputProgramRun (ProgramRun):
    def __init__(self, program_string, input1, input2):
        super().__init__(program_string)
        self.program[1] = input1
        self.program[2] = input2

    def output(self):
        return self.program[0]

if __name__ == '__main__':
    both_parts()