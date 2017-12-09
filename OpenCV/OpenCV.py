import cv2
from Sudoku import Sudoku
from Sudoku import SudokuSolver
import sys


if __name__ == "__main__":
    data = [None] * 81
    for i in range(0, 81):
        ch = sys.stdin.read(1)
        if ch == '.':
            data[i] = 0
        else:
            data[i] = int(ch)

    sudoku = Sudoku(data)

    res = SudokuSolver(sudoku, 0)
    print(sudoku.numbers)