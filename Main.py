from OP_Project import HomeLibrary


def display_menu():
    print("""
    Меню домашньої бібліотеки:
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
    13. Вийти
    """)


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

        if choice == "1":
            add_book_action(library)
        elif choice == "2":
            add_article_action(library)
        elif choice == "3":
            add_magazine_action(library)
        elif choice == "4":
            remove_book_action(library)
        elif choice == "5":
            remove_article_action(library)
        elif choice == "6":
            remove_magazine_action(library)
        elif choice == "7":
            library.list_materials()
        elif choice == "8":
            search_term = input("Введіть пошуковий запит: ")
            library.search_material(search_term)
        elif choice == "9":
            key = input("Введіть критерій сортування (назва, автор, рік): ")
            library.sort_materials(key)
        elif choice == "10":
            library.show_books()
        elif choice == "11":
            library.show_articles()
        elif choice == "12":
            library.show_magazines()
        elif choice == "13":
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
