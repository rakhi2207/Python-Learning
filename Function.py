from book import Book
import json


def options():
    print("Please enter a specific no")
    print("1-Add Book")
    print("2-Save book")
    print("3-Load book")
    print("4-Find book")
    print("5-Issue book")
    print("6-Return book")
    print("7-Update book")
    print("8-Show all book")
    print("9-Show book")


def input_bookinfo():
    id = input("ID : ")
    name = input("Name : ")
    desc = input("Desc : ")
    isbn = input("ISBN : ")
    page_count = int(input("Page Count : "))
    issued = input("Issued y/Y for true or anything else for false ")
    issued = (issued == "y" or issued == "Y")
    author = input("Author : ")
    year = int(input("Year : "))
    return {
        "id": id,
        "name": name,
        "Description": desc,
        "isbn": isbn,
        "page_count": page_count,
        "issued": issued,
        "author": author,
        "year": year
    }


def create_book():
    print("Please enter book details")
    return input_bookinfo()


#
def save(books):
    book_save = []
    for Book in books:
        book_save.append(Book)

        try:
            file = open("books.dat", "w")
            file.write(json.dumps(book_save, indent=4))
        except:
            print("Something is wrong")


def load():
    try:
        books = []
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        for book in loaded_books:
            new_obj = Book(book['id'], book['name'], book['Description'], book['isbn'], book['page_count'],
                           book['issued'],
                           book['author'], book['year'])
            books.append(new_obj.to_dict())
        print("Successfully Loaded")
        return books
    except:
        print("File do not exist or some error occurred")


def find(books):
    id_val = input("Enter book id ")
    for index, book in enumerate(books):
        if book['id'] == id_val:
            return index
    return None


def issue_book(books):
    index = find(books)
    if index is not None:
        books[index]['issued'] = True
        print("Book Successfully issued")
    else:
        print("Book is not available")


def return_book(books):
    index = find(books)
    if index is not None:
        books[index]['issued'] = False
        print("Book Successfully returned")
    else:
        print("Book is not available")


def update_book(books):
    index = find(books)
    if index is not None:
        value = create_book()
        old_book = books[index]
        books[index] = value
        del old_book
        print("Successfully updated ")
    else:
        print("We could not find your book")


def show_all_book(books):
    for book in books:
        print("Id is ",book['id'])
        print("Name is ",book['name'])
        print("Description is ",book['Description'])
        print("ISBN is ",book['isbn'])
        print("Page Count is ",book['page_count'])
        print("Issue status ",book['issued'])
        print("Author is ",book['author'])
        print("Year is ",book['year'])
        print()


def show_book(books):
    index = find(books)
    if index is not None:
        print("Id is ",books[index]['id'])
        print("Name is ",books[index]['name'])
        print("Description is ",books[index]['Description'])
        print("ISBN is ",books[index]['isbn'])
        print("Page Count is ",books[index]['page_count'])
        print("Issue status ",books[index]['issued'])
        print("Author is ",books[index]['author'])
        print("Year is ",books[index]['year'])
        print()
    else:
        print("We could not find your book")
