from model.book import Book

book_list = []


def enroll_book():
    print("\n----- 도서 등록 -----")
    title = input("도서 제목 : ")
    price = input("도서 가격 : ")
    b = Book(title, price)
    book_list.append(b)
    print("등록 완료!")


def print_book_list():
    print("\n----- 도서 목록 -----")
    print("번호 | 제목")
    for idx, b in enumerate(book_list):
        print(f"{idx} | {b.price}")


def print_one_by_one():
    print("\n----- 도서 상세 -----")
    book_num = int(input("조회할 도서 번호 : "))
    d = book_list[book_num]
    print(d)


def delete_book_one_by_one():
    print("\n----- 도서 삭제 -----")
    print("test")
    book_num = int(input("삭제할 도서 번호 : "))
    del book_list[book_num]
