import sys
from pathlib import Path
program_step = 4

def opcode(code, operand1, operand2):
    if code == 1:
        return operand1 + operand2
    elif code == 2:
        return operand1 * operand2

def both_parts():
    program_run = ProgramRun(Path(sys.argv[1]).read_text())
    program_run.run()
    print(str(program_run.output()))

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
        return str(self.program[0])

if __name__ == '__main__':
    both_parts()