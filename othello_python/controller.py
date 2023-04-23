# Othello Controller
from othello_python.model import Board, Stone


class Controller:
    def __init__(self):
        self.board = Board()
        self.turn = Stone("black")

    def run(self):
        while True:
            print(f"{self.turn.color}'s turn")
            print(self.board)
            if not self.board.can_put_anywhere(self.turn):
                print("Cannot put anywhere")
                self.turn = Stone("white" if self.turn.color == "black" else "black")
                continue
            x, y = self.ask_put_position()
            if not self.board.can_put(x, y, self.turn):
                print("Cannot put here")
                continue
            self.board.put(x, y, self.turn)
            self.turn = Stone("white" if self.turn.color == "black" else "black")

    def ask_put_position(self):
        while True:
            x = input("x: ")
            y = input("y: ")
            try:
                x = int(x)
                y = int(y)
                if 0 <= x <= 7 and 0 <= y <= 7:
                    return x, y
                else:
                    print("Out of range")
            except ValueError:
                print("Invalid input")

    def print_result(self):
        black_count = self.board.count(Stone("black"))
        white_count = self.board.count(Stone("white"))
        print(f"Black: {black_count}")
        print(f"White: {white_count}")
        if black_count > white_count:
            print("Black wins!")
        elif black_count < white_count:
            print("White wins!")
        else:
            print("Draw!")
