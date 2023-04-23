# Othello Controller
from othello_python.model import Board, Stone


class Controller:
    def __init__(self):
        self.board = Board()

    # 初手を黒とする
    # 石が置けなくなるまで以下を繰り返す
    # 黒の番か白の番かを出力する
    # ボードの状態を出力する
    # 手番の石を置く場所があるかどうか判断し、置く場所がなければ相手の番とする
    # 置く場所があれば、石を置く場所を尋ねる
    # 指定された場所に石を置けるかBoardクラスを使って判断する
    # 石を置けなければ再度石を置く場所を尋ねる
    # 石を置ければ、Boardクラスを使って石を置いて、相手の番とする
    # 石が置けなくなったら、黒と白の石の数を数えて勝敗を判定する
    def run(self):
        turn = "black"
        while True:
            print(f"{turn}'s turn")
            print(self.board)
            if not self.board.can_put_anywhere(Stone(turn)):
                print(f"{turn} can't put anywhere")
                turn = "white" if turn == "black" else "black"
                continue
            while True:
                x = int(input("row: "))
                y = int(input("column: "))
                if self.board.can_put(x, y, Stone(turn)):
                    self.board.put(x, y, Stone(turn))
                    turn = "white" if turn == "black" else "black"
                    break
                else:
                    print("Can't put there")

            if not self.board.can_put_anywhere(Stone(turn)):
                print(f"{turn} can't put anywhere")
                turn = "white" if turn == "black" else "black"
                continue

            if not self.board.can_put_anywhere(Stone(turn)):
                break

        black_count = self.board.count(Stone("black"))
        white_count = self.board.count(Stone("white"))
        print(f"black: {black_count}, white: {white_count}")
        if black_count > white_count:
            print("black win")
        elif black_count < white_count:
            print("white win")
        else:
            print("draw")
