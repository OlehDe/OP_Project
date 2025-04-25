import datetime

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"Книга: {self.title} автор: {self.author} ({self.year}) - Жанр: {self.genre}"

class Article:
    def __init__(self, title, author, year, journal):
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal

    def __str__(self):
        return f"Стаття: {self.title} автор: {self.author} ({self.year}) - Журнал: {self.journal}"

class Magazine:
    def __init__(self, title, issue, year):
        self.title = title
        self.issue = issue
        self.year = year

    def __str__(self):
        return f"Журнал: {self.title} №: {self.issue} ({self.year})"

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

def display_menu():
    print("""\nМеню домашньої бібліотеки:
1. Додати книгу
2. Додати статтю
3. Додати журнал
4. Видалити книгу
5. Видалити статтю
6. Видалити журнал
7. Переглянути всі матеріали
8. Пошук матеріалу
9. Сортувати матеріали
10. Показати книги
11. Показати статті
12. Показати журнали
13. Вийти""")

def add_book_action(library):
    title = input("Введіть назву книги: ")
    author = input("Введіть ім'я автора: ")
    year = int(input("Введіть рік видання: "))
    genre = input("Введіть жанр книги: ")
    library.add_book(title, author, year, genre)

def add_article_action(library):
    title = input("Введіть назву статті: ")
    author = input("Введіть ім'я автора: ")
    year = int(input("Введіть рік видання: "))
    journal = input("Введіть назву журналу: ")
    library.add_article(title, author, year, journal)

def add_magazine_action(library):
    title = input("Введіть назву журналу: ")
    issue = input("Введіть номер випуску: ")
    year = int(input("Введіть рік видання: "))
    library.add_magazine(title, issue, year)

def remove_book_action(library):
    title = input("Введіть назву книги для видалення: ")
    author = input("Введіть ім'я автора: ")
    library.remove_book(title, author)

def remove_article_action(library):
    title = input("Введіть назву статті для видалення: ")
    author = input("Введіть ім'я автора: ")
    library.remove_article(title, author)

def remove_magazine_action(library):
    title = input("Введіть назву журналу для видалення: ")
    issue = input("Введіть номер випуску: ")
    library.remove_magazine(title, issue)

def main():
    library = HomeLibrary()

    while True:
        display_menu()
        choice = input("Виберіть дію: ")

        if choice == '1':
            add_book_action(library)
        elif choice == '2':
            add_article_action(library)
        elif choice == '3':
            add_magazine_action(library)
        elif choice == '4':
            remove_book_action(library)
        elif choice == '5':
            remove_article_action(library)
        elif choice == '6':
            remove_magazine_action(library)
        elif choice == '7':
            library.list_materials()
        elif choice == '8':
            search_term = input("Введіть пошуковий запит: ")
            library.search_material(search_term)
        elif choice == '9':
            key = input("Введіть критерій сортування (назва, автор, рік): ")
            library.sort_materials(key)
        elif choice == '10':
            library.show_books()
        elif choice == '11':
            library.show_articles()
        elif choice == '12':
            library.show_magazines()
        elif choice == '13':
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
