# try:
import json

from book import Book


def write_to_file():
    with open("data.txt", "w", encoding="utf-8") as f:
        title = input("title : ")
        price = int(input("price : "))
        book = Book(title, price)
        json.dump(book.to_dict(), f, ensure_ascii=False, indent=4)
def read_from_file():
    with open("data.txt", "r", encoding="utf-8") as f:
        d = json.load(f)
        print(d)
        book = Book.from_dict(d)
        print("book : ", book)
        print("type(book) : ", type(book))

print("1 write")
print("2 read")
num = int(input("메뉴 번호 : "))
match num:
    case 1:
        write_to_file()
    case 2:
        read_from_file()
# finally:
#     f.close()