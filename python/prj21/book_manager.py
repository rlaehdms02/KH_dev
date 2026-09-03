from model.book import Book
book_list = []

def print_menu():
    print("0. Shutdown")
    print("1. Add Book")
    print("2. Select Book")
    print("3. Select One Book")
    print("4. Remove Book")

def scan_user_input():
    return int(input("Menu Number : "))
def process(num):
    match num:
        case 0:
            return False
        case 1:
            enroll_book()
        case 2:
            select_book_list()
        case 3:
            select_book_one()
        case 4:
            remove_book()
        case _:
            print("Please try again")
    return True


def enroll_book():
    print("-----Insert Book-----")
    title = input("Enter Book Title : ")
    author = input("Enter Book Author : ")
    book = Book(title, author)
    book_list.append(book)
    print("Inserted Book OK")
def select_book_list():
    print("-----Select Book List-----")
    for idx, book in enumerate(book_list):
        print(f"{idx+1}. {book.title}")
    print("-----End-----")

def select_book_one():
    print("-----Select Book One-----")
    select_number = int(input("Select Book Number : "))
    print(book_list[select_number-1])
    print("-----End-----")

def remove_book():
    print("-----Remove Book-----")
    Remove_number = int(input("Remove Book Number : "))
    del book_list[Remove_number-1]
    print("Removed Book OK")