class Article:
    def __init__(self, title, author, year, journal):
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal

    def __str__(self):
        return f"Стаття: {self.title} автор: {self.author} ({self.year}) - Журнал: {self.journal}"