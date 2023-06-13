from setup import Puzzle, Id, Digit

puz = Puzzle()

puz.set_square0(Id(6), Id(7), Digit(6))
print(puz.get_square(Id(6), Id(4)).val)
print(puz.get_square(Id(6), Id(7)).val)
puz.update_possible_squares()
print(puz.get_square(Id(6), Id(4)).val)
print(puz.get_square(Id(6), Id(7)).val)