import sys

entity_wire1 = 1
entity_wire2 = 2
entity_origin = 0

def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

class WireBoard:
    board = []
    def __init__(self, description):
        board = [[[],[],[]],[[],[],[]],[[],[],[]]]

    def __str__(self):
        return str(board)

if __name__ == '__main__':
    print(sys.argv[1])