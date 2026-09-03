import json

from book.model.book import Book


def print_menu() -> None:
    print("0. exit")
    print("1. car insert")
    print("2. select list")
    print("3. select one")
    print("4. remove car")
    print("5. edit")

def scan_menu_num() -> int:
    num = int(input("menu num : "))
    return num


def insert():
    book_list = select_list()
    with open("book_data.json", "w", encoding="utf-8") as f:
        title = input("title : ")
        author = input("author : ")
        price = input("price : ")
        book = Book(title, author ,price)
        book_dict = book.to_dict()
        book_list.append(book_dict)
        json.dump(book_list, f, ensure_ascii=False, indent=2)

def select_list():
    try:
        with open("book_data.json", "r", encoding="utf-8") as f:
            book_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        book_list = []  # 파일이 없거나 내용이 비어있으면 빈 리스트 반환
    return book_list

def print_book_list(book_list) -> None:
    for x in book_list:
        book = Book.from_dict(x)
        print(book)

def select_one():
    pass


def remove():
    pass


def edit():
    pass


def process(num: int) -> None:
    match num:
        case 1: insert()
        case 2:
            book_list = select_list()
            print_book_list(book_list)
        case 3: select_one()
        case 4: remove()
        case 5: edit()

def program_start():
    while True:
        try:
            print_menu()
            num = scan_menu_num()
            if num == 0: break
            process(num)
        except  ArithmeticError as e:
            print(e)