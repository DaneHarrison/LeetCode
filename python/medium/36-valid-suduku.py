import math

def isValidSudoku(self, board: List[List[str]]) -> bool:
    size = len(board)
    
    if size % 3 != 0:
        return False

    cols = [set() for x in board]
    squares = {}

    for yIdx, line in enumerate(board):
        invalidSize = len(line) != size
        rowNumbers = [x for x in line if x != "."]
        rowHasDupes = len(rowNumbers) != len(set(rowNumbers))

        if invalidSize or rowHasDupes:
            return False
        
        for xIdx, num in enumerate(line):
            if num == ".":
                continue

            xKey = math.floor(xIdx / 3)
            yKey = math.floor(yIdx / 3)
            squareKey = f'{yKey},{xKey}'
            seen = squares.get(squareKey, set())

            if num in seen:
                return False
            else:
                seen.add(num)
                squares[squareKey] = seen

            if num in cols[xIdx]:
                return False
            else:
                cols[xIdx].add(num)

    return True