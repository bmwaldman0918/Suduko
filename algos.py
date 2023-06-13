from setup import Puzzle, Square, Digit
from copy import deepcopy

class Naive:
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

class SecondPass:
    def secondpass(p: Puzzle) -> bool:
        while not p.finished():
            same = True
            prev = deepcopy(p.squares)
            p.update_possible_squares()
            for s in p.squares:
                SecondPass.secondpass_util(p, s)
            for prev_square in prev:
                row = prev_square.row.id
                col = prev_square.col.id
                curr_square = p.get_square(row, col)
                if prev_square.val != curr_square.val:
                    same = False
            if same == True:
                return False
        return True
    
    def secondpass_util(p: Puzzle, s: Square):
        if isinstance(s.val, Digit):
            return None
        
        for pos_val in s.val:
            row = True
            for r in s.row.squares:
                if isinstance(r.val, Digit):
                    continue
                if pos_val in r.val:
                    row = False
            if row:
                p.set_square1(s, pos_val)
                return
        
            col = True
            for r in s.col.squares:
                if isinstance(r.val, Digit):
                    continue
                if pos_val in r.val:
                    col = False
            if col:
                p.set_square1(s, pos_val)
                return

            box = True
            for r in s.box.squares:
                if isinstance(r.val, Digit):
                    continue
                if pos_val in r.val:
                    box = False
            if box:
                p.set_square1(s, pos_val)
                return