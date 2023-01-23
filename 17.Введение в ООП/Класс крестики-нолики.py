class TicTacToeBoard:

    def __init__(self):
        self.map = [['-' for _ in range(3)] for _ in range(3)]
        self.hod = 0
        self.mest = ''
        self.proverka = False

    def new_game(self):
        self.map = [['-' for _ in range(3)] for _ in range(3)]
        self.hod = 0
        self.mest = ''
        self.proverka = False

    def get_field(self):
        return self.map

    def make_move(self, x, y):
        if self.map[x - 1][y - 1] != 'X':
            if self.map[x - 1][y - 1] != '0':
                if self.hod / 2 == self.hod // 2:
                    self.map[x - 1][y - 1] = 'X'
                else:
                    self.map[x - 1][y - 1] = '0'
                self.hod += 1
                if self.mest == '':
                    if self.check_field() == 'X':
                        self.proverka = True
                        return self.mest
                    elif self.check_field() == '0':
                        self.proverka = True
                        return self.mest
                    else:
                        return 'Продолжаем играть'
        if self.proverka:
            return 'Игра уже завершена'
        else:
            return 'Клетка' + ' ' + str(x) + ',' + ' ' + str(y) + ' ' + 'уже занята'

    def check_field(self):
        for i in self.map:
            if self.map[0][0] == self.map[0][1] == self.map[0][2] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[1][0] == self.map[1][1] == self.map[1][2] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[2][0] == self.map[2][1] == self.map[2][2] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[0][0] == self.map[1][1] == self.map[2][2] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[0][2] == self.map[1][1] == self.map[2][0] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[0][0] == self.map[1][0] == self.map[2][0] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[0][1] == self.map[1][1] == self.map[2][1] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[0][2] == self.map[1][2] == self.map[2][2] == 'X':
                self.mest = 'Победил игрок X'
                return 'X'
            if self.map[0][0] == self.map[0][1] == self.map[0][2] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            if self.map[1][0] == self.map[1][1] == self.map[1][2] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            if self.map[2][0] == self.map[2][1] == self.map[2][2] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            if self.map[0][0] == self.map[1][1] == self.map[2][2] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            if self.map[0][2] == self.map[1][1] == self.map[2][0] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            if self.map[0][0] == self.map[1][0] == self.map[2][0] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            if self.map[0][1] == self.map[1][1] == self.map[2][1] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            if self.map[0][2] == self.map[1][2] == self.map[2][2] == '0':
                self.mest = 'Победил игрок 0'
                return '0'
            else:
                return None


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 2))
print(board.make_move(1, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(3, 3))
print(*board.get_field(), sep="\n")
print(board.make_move(3, 3))
print(board.make_move(2, 2))
print(board.make_move(3, 2))
print(*board.get_field(), sep="\n")