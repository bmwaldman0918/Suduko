from setup import Puzzle, Id, Digit

class Util:
    def run_test(p: Puzzle, algo):
        print("Puzzle")
        print(p)
        success = algo(p)

        if success:
            print("Solution:")
        else:
            print("The algorithm terminated at:")
        print(p)

class Easy:
    def easy1() -> Puzzle:
        puz = Puzzle()

        # row 1
        puz.set_square0(Id(1), Id(1), Digit(1))
        puz.set_square0(Id(1), Id(2), Digit(3))
        puz.set_square0(Id(1), Id(4), Digit(4))
        puz.set_square0(Id(1), Id(5), Digit(6))
        puz.set_square0(Id(1), Id(8), Digit(5))

        # row 2
        puz.set_square0(Id(2), Id(4), Digit(8))
        puz.set_square0(Id(2), Id(7), Digit(2))
        puz.set_square0(Id(2), Id(8), Digit(1))
        puz.set_square0(Id(2), Id(9), Digit(3))

        # row 3
        puz.set_square0(Id(3), Id(2), Digit(2))
        puz.set_square0(Id(3), Id(4), Digit(5))
        puz.set_square0(Id(3), Id(9), Digit(6))

        # row 4
        puz.set_square0(Id(4), Id(1), Digit(5))
        puz.set_square0(Id(4), Id(2), Digit(7))
        puz.set_square0(Id(4), Id(6), Digit(1))
        puz.set_square0(Id(4), Id(7), Digit(3))

        # row 5
        puz.set_square0(Id(5), Id(4), Digit(7))
        puz.set_square0(Id(5), Id(5), Digit(3))
        puz.set_square0(Id(5), Id(6), Digit(4))

        # row 6
        puz.set_square0(Id(6), Id(3), Digit(8))
        puz.set_square0(Id(6), Id(4), Digit(2))
        puz.set_square0(Id(6), Id(8), Digit(4))
        puz.set_square0(Id(6), Id(9), Digit(7))

        # row 7
        puz.set_square0(Id(7), Id(1), Digit(9))
        puz.set_square0(Id(7), Id(6), Digit(5))
        puz.set_square0(Id(7), Id(8), Digit(2))

        # row 8
        puz.set_square0(Id(8), Id(1), Digit(2))
        puz.set_square0(Id(8), Id(2), Digit(6))
        puz.set_square0(Id(8), Id(3), Digit(5))
        puz.set_square0(Id(8), Id(6), Digit(8))

        # row 9
        puz.set_square0(Id(9), Id(2), Digit(4))
        puz.set_square0(Id(9), Id(5), Digit(2))
        puz.set_square0(Id(9), Id(6), Digit(9))
        puz.set_square0(Id(9), Id(8), Digit(8))
        puz.set_square0(Id(9), Id(9), Digit(1))

        return puz
