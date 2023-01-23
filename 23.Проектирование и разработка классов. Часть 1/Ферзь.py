class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row1, col1):
        if not (0 <= row1 < 8 and 0 <= col1 < 8):
            return False
        if abs(row1 - self.row) == abs(col1 - self.col):
            return True
        if self.row != row1 and self.col != col1:
            return False
        return True

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][3] = Queen(WHITE)
queen = board.get_piece(0, 3)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, 0, 3, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()