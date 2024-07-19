"""
state is a sequence of moves in a python list
each move will be modeled as an integer between 0 and 8 inclusive
validation: must be an integer in range that hasnt been selected
add_move(moves, m) -> True/False
    - validate move
    - append m to moves
check_winner(moves) -> 0, 1 or None
    - deinterleave played moves into those played by player 0 and 1 e.g [0, 9, 1,8,2]
    would become [0,1,2] and [9,8]
    - treat each player's moves as sets
    - compare played moves to victory condition move sets, e.g {0,1,2} would be a horizontal victory
    - subtracting played set from victory condition set results in an empty or non-empty set...
    if empty, that player has won
    - 8 victory conditions -> 3 horizontal, 3 vertical, 2 diagonal
print_board(moves)
    - reformat 1 x 9 list as 3 x 3 grid for printing
    - have default items of A to I so next player can select which square to play
    - for each move that has been made, overwrite the placeholder letter with x or o
next_player(moves)
    - len(moves) % 2
"""

import os

VICTORY_CONDITIONS = (
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},  # horizontal
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},  # vertical
    {0, 4, 8},
    {2, 4, 6},  # diagonal
)

PLAYER_SYMBOLS = ("X", "O")


class Game(object):
    def __init__(self):
        self.moves = []

    def __str__(self):
        board = list("abcdefghi")
        for i, m in enumerate(self.moves):
            board[m] = PLAYER_SYMBOLS[i % 2]

        return "\n---+---+---\n".join(
            "|".join(f" {c} " for c in row)
            for row in (board[0:3], board[3:6], board[6:9])
        )

    def winner(self):
        for i, played in enumerate((set(self.moves[::2]), set(self.moves[1::2]))):
            for needed in VICTORY_CONDITIONS:
                if len(needed - played) == 0:
                    return i

    # The ord function in Python is used to convert
    # a single character into its corresponding Unicode code point,
    # which is an integer
    # representing the character in the Unicode standard.

    def add_move(self, m):
        try:
            mi = ord(m.lower()) - ord("a")
            assert 0 <= mi < 9
            assert mi not in self.moves
        except (AttributeError, TypeError, AssertionError):
            return False
        self.moves.append(mi)
        return True

    def next_player(self):
        return len(self.moves) % 2


if __name__ == "__main__":
    g = Game()
    while g.winner() is None:
        os.system("clear")
        print(g)
        while True:
            m = input(f"Player {PLAYER_SYMBOLS[g.next_player()]} turn: ")
            if g.add_move(m):
                break
            print("Invalid move!")

    print(g)
    print(f"Player {PLAYER_SYMBOLS[g.winner()]} wins!")
    print("ok")
