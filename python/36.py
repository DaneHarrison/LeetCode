from collections import defaultdict
from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    size = len(board)
    cols = [set() for _ in range(size)]
    squares = defaultdict(set)

    for i in range(size):
        row = board[i]
        filteredRow = [c for c in row if c != "."]

        if len(filteredRow) != len(set(filteredRow)):
            return False

        for j in range(size):
            if board[i][j] == ".":
                continue

            # check columns
            if board[i][j] in cols[j]:
                return False

            cols[j].add(board[i][j])

            squareX = i // 3
            squareY = j // 3
            squareIdx = f"{squareX},{squareY}"

            # check square - index is top left position of each square
            if board[i][j] in squares[squareIdx]:
                return False

            squares[squareIdx].add(board[i][j])

    return True