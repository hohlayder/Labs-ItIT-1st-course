class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'


b = Book('Последнее желание', 'Анджей Сапковский', 1993)
print(b.get_info())