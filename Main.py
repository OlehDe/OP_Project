from HomeLib import HomeLibrary

def display_menu():
    print("""
    Меню домашньої бібліотеки:
    1. Додати
    2. Видалити
    3. Переглянути всі матеріали
    4. Пошук матеріалу
    5. Сортувати матеріали
    6. Показати
    7. Вийти
    """)

def add_menu():
    print("""
    1. Додати книгу
    2. Додати статтю
    3. Додати журнал
    """)

def remove_menu():
    print("""
    1. Видалити книгу
    2. Видалити статтю
    3. Видалити журнал
    """)

def see_menu():
    print("""
    1. Показати книги
    2. Показати статті
    3. Показати журнали
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
            add_menu()
            choice = input("Виберіть дію: ")
            if choice == "1":
                add_book_action(library)
            elif choice == "2":
                add_article_action(library)
            elif choice == "3":
                add_magazine_action(library)
            else:
                print("Невірний вибір, спробуйте ще раз.")
        elif choice == "2":
            remove_menu()
            choice = input("Виберіть дію: ")
            if choice == "1":
                remove_book_action(library)
            elif choice == "2":
                remove_article_action(library)
            elif choice == "3":
                remove_magazine_action(library)
        elif choice == "3":
            library.list_materials()
        elif choice == "4":
            search_term = input("Введіть пошуковий запит: ")
            library.search_material(search_term)
        elif choice == "5":
            key = input("Введіть критерій сортування (title, author, year): ")
            library.sort_materials(key)
            library.list_materials()
        elif choice == "6":
            see_menu()
            choice = input("Виберіть тип матеріалу для перегляду: ")
            if choice == "1":
                library.show_books()
            elif choice == "2":
                library.show_articles()
            elif choice == "3":
                library.show_magazines()
        elif choice == "7":
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
