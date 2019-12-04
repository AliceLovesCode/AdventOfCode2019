import sys

entity_wire1 = 1
entity_wire2 = 2
entity_origin = 0

def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

class WireBoard:
    board = [[[],[],[]],[[],[],[]],[[],[],[]]]
    def __init__(self, description):
        self.board = self.parse_description(description)

    def parse_description(self, description):
        wires = description.split('\n')
        segments = [x.split(',') for x in wires]
        print(segments)
        return segments

    def calculate_board_extent(self, segments):
        print('no')

    def __str__(self):
        return str(self.board)

if __name__ == '__main__':
    board = WireBoard("R8,U5,L5,D3\nU7,R6,D4,L4")
    print(board)