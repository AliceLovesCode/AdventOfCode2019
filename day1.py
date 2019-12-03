import math
import sys
from pathlib import Path

def module_fuel_required(module_mass):
    return math.floor(module_mass / 3) - 2

def total_fuel_required(module_masses):
    module_fuel_quantities = [module_fuel_required(x) for x in module_masses]
    return sum(module_fuel_quantities)

def load_masses_file(filename):
    file_data = [int(x) for x in Path(filename).read_text().split('\n')]
    return total_fuel_required(file_data)

if __name__ == '__main__':
    print(load_masses_file(sys.argv[1]))