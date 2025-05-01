import datetime

from Article import Article
from Book import Book
from Magazine import Magazine


class HomeLibrary:
    def __init__(self):
        self.books = []
        self.articles = []
        self.magazines = []

        self.add_book("Молоді серця", "Іван Франко", 1890, "Роман")
        self.add_article("Штучний інтелект", "Юрій Мельниченко", 2023, "Наука та життя")
        self.add_article("Сучасні технології", "Олена Коваленко", 2022, "Техно-Майбутнє")
        self.add_magazine("Наука і прогрес", "1", 2024)
        self.add_magazine("Математика та фізика", "5", 2023)

    def add_book(self, title, author, year, genre):
        if not self.validate_year(year):
            print("Невірний рік!")
            return
        if self.check_duplicate(title, author):
            print("Ця книга вже існує!")
            return
        if len(title) > 100 or len(author) > 50:
            print("Назва або ім'я автора занадто довгі!")
            return
        new_book = Book(title, author, year, genre)
        self.books.append(new_book)
        print(f"Книгу '{title}' додано.")

    def add_article(self, title, author, year, journal):
        if not self.validate_year(year):
            print("Невірний рік!")
            return
        if self.check_duplicate(title, author):
            print("Ця стаття вже існує!")
            return
        if len(title) > 100 or len(author) > 50:
            print("Назва або ім'я автора занадто довгі!")
            return
        new_article = Article(title, author, year, journal)
        self.articles.append(new_article)
        print(f"Статтю '{title}' додано.")

    def add_magazine(self, title, issue, year):
        if not self.validate_year(year):
            print("Невірний рік!")
            return
        if len(title) > 100:
            print("Назва занадто довга!")
            return
        new_magazine = Magazine(title, issue, year)
        self.magazines.append(new_magazine)
        print(f"Журнал '{title}' додано.")

    def remove_book(self, title, author):
        for book in self.books:
            if book.title == title and book.author == author:
                self.books.remove(book)
                print(f"Книгу '{title}' видалено.")
                return
        print(f"Книгу '{title}' не знайдено.")

    def remove_article(self, title, author):
        for article in self.articles:
            if article.title == title and article.author == author:
                self.articles.remove(article)
                print(f"Статтю '{title}' видалено.")
                return
        print(f"Статтю '{title}' не знайдено.")

    def remove_magazine(self, title, issue):
        for magazine in self.magazines:
            if magazine.title == title and magazine.issue == issue:
                self.magazines.remove(magazine)
                print(f"Журнал '{title}' видалено.")
                return
        print(f"Журнал '{title}' не знайдено.")

    def list_materials(self):
        print("\nКниги:")
        for book in self.books:
            print(book)
        print("\nСтатті:")
        for article in self.articles:
            print(article)
        print("\nЖурнали:")
        for magazine in self.magazines:
            print(magazine)

    def search_material(self, search_term):
        print("\nРезультати пошуку:")
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                print(book)
        for article in self.articles:
            if search_term.lower() in article.title.lower() or search_term.lower() in article.author.lower():
                print(article)
        for magazine in self.magazines:
            if search_term.lower() in magazine.title.lower():
                print(magazine)

    def sort_materials(self, key):
        self.books.sort(key=lambda x: getattr(x, key))
        self.articles.sort(key=lambda x: getattr(x, key))
        self.magazines.sort(key=lambda x: getattr(x, key))
        print(f"Відсортовано за {key}.")

    def validate_year(self, year):
        current_year = datetime.datetime.now().year
        return isinstance(year, int) and 1800 <= year <= current_year

    def check_duplicate(self, title, author):
        for book in self.books:
            if book.title == title and book.author == author:
                return True
        for article in self.articles:
            if article.title == title and article.author == author:
                return True
        for magazine in self.magazines:
            if magazine.title == title:
                return True
        return False

    def show_books(self):
        print("\nКниги в бібліотеці:")
        for book in self.books:
            print(book)

    def show_articles(self):
        print("\nСтатті в бібліотеці:")
        for article in self.articles:
            print(article)

    def show_magazines(self):
        print("\nЖурнали в бібліотеці:")
        for magazine in self.magazines:
            print(magazine)


