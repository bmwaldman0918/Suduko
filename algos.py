from setup import Puzzle
from copy import deepcopy

def naive(p: Puzzle) -> bool:
    while not p.finished():
        same = True
        prev = deepcopy(p.squares)
        p.update_possible_squares()
        for prev_square in prev:
            row = prev_square.row.id
            col = prev_square.col.id
            curr_square = p.get_square(row, col)
            if prev_square.val != curr_square.val:
                same = False
        if same == True:
            return False
    return True
