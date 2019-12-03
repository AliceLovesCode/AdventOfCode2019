import math
import sys
from pathlib import Path

def mass_fuel_required(mass):
    return math.floor(mass / 3) - 2

def part1_summed_fuel_required(module_masses):
    module_fuel_quantities = [mass_fuel_required(x) for x in module_masses]
    return sum(module_fuel_quantities)

def part2_summed_fuel_required(module_masses):
    module_fuel_quantities = [recursive_fuel_required(x) for x in module_masses]
    return sum(module_fuel_quantities)

def recursive_fuel_required(mass):
    fuel_required = mass_fuel_required(mass)
    if fuel_required <= 0:
        return 0
    else: 
        return fuel_required + recursive_fuel_required(fuel_required)
    

def load_masses_file(filename):
    return [int(x) for x in Path(filename).read_text().split('\n')]

def do_parts(input_file):
    masses = load_masses_file(input_file)
    print("Day 1 Part 1 fuel calculation: {0}\n".format(part1_summed_fuel_required(masses)))
    print("Day 1 Part 2 fuel calculation: {0}\n".format(part2_summed_fuel_required(masses)))

if __name__ == '__main__':
    do_parts(sys.argv[1])