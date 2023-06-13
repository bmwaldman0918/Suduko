from enum import IntEnum
import copy

class Puzzle:

    def __init__(self):
        self.rows = dict()
        self.cols = dict()
        self.boxes = dict()
        self.squares = set()

        for i in list(Id):
            self.rows[i] = Group(GroupType.ROW, i)
            self.cols[i] = Group(GroupType.COLUMN, i)
            self.boxes[i] = Group(GroupType.BOX, i)
        
        for row in list(Id):
            for col in list(Id):
                if row < 4 and col < 4:
                    box = self.boxes[1]
                elif row < 4 and col < 7:
                    box = self.boxes[2]
                elif row < 4:
                    box = self.boxes[3]
                elif row < 7 and col < 4:
                    box = self.boxes[4]
                elif row < 7 and col < 7:
                    box = self.boxes[5]
                elif row < 7:
                    box = self.boxes[6]
                elif col < 4:
                    box = self.boxes[7]
                elif col < 7:
                    box = self.boxes[8]
                else:
                    box = self.boxes[9]

                curr_row = self.rows[row]
                curr_col = self.cols[col]

                square = Square(curr_row, curr_col, box, [Digit(i) for i in range(1, 10)])
                box.squares.append(square)
                curr_col.add_square(square)
                curr_row.add_square(square)
                self.squares.add(square)
            
    def set_square0(self, row, col, val):
        assert(isinstance(row, Id))
        assert(isinstance(col, Id))
        assert(isinstance(val, Digit))

        square = self.get_square(row, col)
        square.val = val
        square.row.unused.remove(val)
        square.col.unused.remove(val)
        square.box.unused.remove(val)

    def set_square1(self, square, val):
        assert(isinstance(square, Square))
        assert(isinstance(val, Digit))

        square.val = val
        square.row.unused.remove(val)
        square.col.unused.remove(val)
        square.box.unused.remove(val)

    def get_square(self, row, col):
        assert(isinstance(row, Id))
        assert(isinstance(col, Id))

        squares = self.rows[row].squares

        for i in squares:
            if i.col.id == col:
                return i
            
    def update_possible_squares(self):
        for square in self.squares:
            val = square.val
            if isinstance(val, Digit):
                continue
            for pos_val in copy.copy(val):
                if (pos_val not in square.row.unused) or (pos_val not in square.col.unused) or (pos_val not in square.box.unused):
                    val.remove(pos_val)
            if len(val) == 1:
                self.set_square1(square, val[0])
    
    def finished(self) -> bool:
        for s in self.squares:
            if not isinstance(s.val, Digit):
                return False
        return True
    
    def __str__(self) -> str:
        s = ""
        blank_line = str(" " * 11) + '\n'
        for row in range(1, 10):
            for col in range(1, 10):
                square = self.get_square(Id(row), Id(col))
                if isinstance(square.val, Digit):
                    s = s + str(square.val)
                else:
                    s = s + '\x1B[4m' + str(len(square.val)) + '\x1B[0m'
                if col % 3 == 0:
                    s = s + ' '
            s = s + '\n'
            if row % 3 == 0:
                s = s + blank_line
        return s


class Group:

    def __init__(self, group_type, id):
        assert(isinstance(group_type, GroupType))
        assert(isinstance(id, Id))

        self.group_type = group_type
        self.id = id
        self.unused = [Digit(i) for i in range(1, 10)]
        self.squares = list()
    
    def add_square(self, s):
        assert(isinstance(s, Square))
        self.squares.append(s)

class Square:

    def __init__(self, row: Group, col: Group, box: Group, val):
        assert(row.group_type == GroupType.ROW)
        assert(col.group_type == GroupType.COLUMN)
        assert(box.group_type == GroupType.BOX)

        self.row = row
        self.col = col
        self.box = box
        self.val = val

class GroupType(IntEnum):
    ROW = 1
    COLUMN = 2
    BOX = 3

class Id(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

class Digit(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9