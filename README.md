OP_Project

   Варіант 1. Домашня бібліотека

   Написати програму, яка буде імітувати домашню бібліотеку. Вона
повинна зберігати такі матеріали як книги, статті та журнали.
   Потрібно забезпечити наступні можливості для роботи з
бібліотекою:
   1. додавання книги, статті або журналу;
   2. видалення книги, статті або журналу;
   3. перегляд переліку книг, статей та журналів;
   4. пошук книги, статті або журналу за будь-якою властивістю
(наприклад, за автором або за роком видання);
   5. сортування книг, статей або журналів за властивостями.
   6. метод для виведення тільки одного з типів матеріалу.
  
  Потрібно описати наступні класи:

   1. Book(книга) - клас, який представлятиме книгу і містить всі необхідні атрибути та методи.
   2. Article(стаття) - клас, який представлятиме статтю та буде містити необхідні атрибути та методи.
   3. Magazine(журнал) - клас, який представлятиме журнал та буде містити необхідні атрибути та методи.
   4. HomeLibrary(Домашня бібліотека) - клас, який буде зберігати та управляти книгами, статтями та журналами, які в ньому збережені.

Валідація даних:

   Перевірка правильності року видання. Напишіть метод, який буде
перевіряти, чи введений рік видання є коректним цілим числом і чи не
перевищує він поточний рік.
   Перевірка унікальності книг за назвою та автором. Напишіть
метод, який перед створенням нового обʼєкта перевіряє, чи не існує вже
книга/стаття/журнал з такою ж назвою та автором у бібліотеці перед
додаванням нового матеріалу.
   Обмеження на довжину назви та автора. Напишіть обмеження на
довжину назви книги та імені автора, яке не дозволяє вводити текст
довшим за певну кількість символів.