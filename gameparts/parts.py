class Board:
    '''Класс, который описывает игровое поле.'''

    field_size = 3

    def __init__(self):
        '''Инициализирует шаблон игрового поля.'''
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        '''Делает ход согласно "координатам"
        переданным при вызове метода.'''
        self.board[row][col] = player

    def display(self):
        '''Отрисовывает игровое поле в консоли,
        согласно шаблону __init__.'''
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        '''Переопределили метод, добавили описание класса.'''
        return (
            'Обьект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
