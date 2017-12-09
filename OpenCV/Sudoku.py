class Sudoku():
    """description of class"""
    numbsers = []

    def __init__(self, numbers):
        if len(numbers) != 81:
            print("Sudoku numbers count error!!!")
        else:
            self.numbers = list(numbers)

    def SudokuSolver(self):
        return self.PartitionSolver(0)

    def PartitionSolver(self, index):
        if index == 81:
            return True

        if self.numbers[index] != 0:
            return self.PartitionSolver(index + 1)

        valid = self.getValid(index)

        for i in valid:
            self.numbers[index] = i
            if self.PartitionSolver(index + 1):
                return True

        self.numbers[index] = 0
        return False

    def getValid(self, index):
        
        if index >= 81 or index < 0:
            print("Sudoku index error.")
            return set()

        if self.numbers[index] != 0:
            print("Sudoku number in index is already set.")
            return set()
        result = set([1,2,3,4,5,6,7,8,9])

        a = index / 9
        b = index % 9
        for i in range(9 * a, 9 * a + 9):
            if self.numbers[i] in result:
                result.remove(self.numbers[i])

        for i in range(b, 81 + b, 9):
            if self.numbers[i] in result:
                result.remove(self.numbers[i])

        for i in range(a/3*3, a/3*3 +3):
            for j in range(b/3*3, b/3*3 +3):
                if self.numbers[9*i + j] in result:
                    result.remove(self.numbers[9*i + j])

        return result


