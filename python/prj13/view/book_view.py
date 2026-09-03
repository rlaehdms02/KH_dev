from model.book_service import enroll_book, print_book_list, delete_book_one_by_one, print_one_by_one


def print_menu():
    print("1.도서 등록\n2.도서 조회\n3.도서 상세조회\n4.삭제하기")


def procese(menu_num):
    match menu_num:
        case "0":
            return True
        case "1":
            enroll_book()
        case "2":
            print_book_list()
        case "3":
            print_one_by_one()
        case "4":
            delete_book_one_by_one()
        case _:
            print("잘못 입력하셨습니다.")

def scan_user_menu():
    menu_num = input("메뉴 번호")
    return menu_num