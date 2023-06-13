sudoko algorithm

class: group has a group_type, an id, 9 squares, and a set of unused digits
enum: group_type is a row/col/box
class: square has 3 classes, one row, one col, and one box and a value
enum: digit int from 1-9
enum: id int from 1-9
value: type that is either a digit or set of digits

second pass: for each group, check if another box can take that number, if no, it must be this box's

brute force: sort by smallest possible values
- create sub-puzzles: choose a val at random, assign it and see what the algo gives back
- cases: 
    1: algo solved the puzzle! yay, return that puzzle
    2: algo doesn't terminate: do the same on sub-cases
    3: algo fails (inidcated by a square having no possible options): remove that digit as a possibility for puzzle one level up