import cv2
import Sudoku
import sys
def solve(sudoku, index):
    if index == 81:
        return True

    if sudoku.numbers[index] != 0:
        return solve(sudoku, index + 1)

    valid = sudoku.getValid(index)

    for i in valid:
        sudoku.numbers[index] = i
        if solve(sudoku, index + 1):
            return True

    sudoku.numbers[index] = 0
    return False

if __name__ == "__main__":
    data = [None] * 81
    for i in range(0, 81):
        ch = sys.stdin.read(1)
        if ch == '.':
            data[i] = 0
        else:
            data[i] = int(ch)

    sudoku = Sudoku.Sudoku(data)

    res = solve(sudoku, 0)
    print(sudoku.numbers)
