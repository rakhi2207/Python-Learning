import Function
import os

Function.options()
val = input()
books = []
books_id = []
while val != "x" and val != "X":

    if val == "1":
        try:
            book=Function.create_book()
            if book['id'] not in books_id:
                books.append(book)
                books_id.append(book['id'])
            else:
                raise Exception("Id already exist")
        except Exception as e:
            print()
            print(e)
            print()

    elif val == "2":
        Function.save(books)

    elif val == "3":
        books = Function.load()

    elif val == "4":
        print(Function.find(books))

    elif val == "5":
        Function.issue_book(books)

    elif val == "6":
        Function.return_book(books)

    elif val == "7":
        Function.update_book(books)

    elif val == "8":
        Function.show_all_book(books)

    elif val == "9":
        Function.show_book(books)

    os.system("clear")
    Function.options()
    val = input()
