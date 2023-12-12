class FieldIndexError(IndexError):
    '''Переопределяет __str__ в случае исключения IndexError'''

    def __str__(self):
        return 'Введено значение за границами игрового поля'
