class Book:
    def __init__(self, title, authors, publication_year):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year

    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)

books = [Book('Introduction to Algorithms (1st ed.)',
            ['Cormen', 'Leiserson'],
            2007),
            Book('Introduction to Algorithms (2nd ed.)',
            ['Cormen', 'Leiserson', 'Rivest'],
            2008),
            Book('Introduction to Algorithms (3rd ed.)',
            ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
            2009)]

books.sort(key=Book.num_authors, reverse=True)

for book in books: print(book)