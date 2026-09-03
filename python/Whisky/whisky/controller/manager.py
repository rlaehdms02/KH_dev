import json

from whisky.model.whisky import Whisky
def print_menu() -> None:
    print("0. exit")
    print("1. 위스키 등록")
    print("2. 위스키 리스트")
    print("3. 상세조회")
    print("4. 삭제하기")
    print("5. 수정")

def scan_menu_num() -> int:
    num = int(input("menu num : "))
    return num


def insert():
    Whisky_list = select_list()
    with open("Whisky_data.json", "w", encoding="utf-8") as f:
        whisky_name = input("Whisky : ")
        for x in Whisky_list:
            if x["위스키"] == whisky_name:
                print(f"이미 등록된 위스키입니다. '{whisky_name}'")
                return
        whisky_year = input("Whisky year : ")
        price = input("price : ")
        Whisky_data = Whisky(whisky_name, whisky_year ,price)
        Whisky_dict = Whisky_data.to_dict()
        Whisky_list.append(Whisky_dict)
        json.dump(Whisky_list, f, ensure_ascii=False, indent=2)

def select_list():
    try:
        with open("Whisky_data.json", "r", encoding="utf-8") as f:
            Whisky_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        Whisky_list = []
    return Whisky_list

def print_book_list(Whisky_list) -> None:
    for i, x in enumerate(Whisky_list, start=1):
        whisky = Whisky.from_dict(x)
        print(f"{i}. {whisky}")

def select_one():
    Whisky_list = select_list()
    if not Whisky_list:
        print("등록된 위스키가 없습니다.")
        return
    whisky_number = int(input("위스키 번호 : "))
    if 1 <= whisky_number <= len(Whisky_list):
        whisky_data = Whisky_list[whisky_number-1]
        whisky = Whisky.from_dict(whisky_data)
        print(whisky)
    else:
        print("존재하지 않는 위스키 번호입니다.")

def remove():
    Whisky_list = select_list()
    if not Whisky_list:
        print("등록된 위스키가 없습니다.")
        return
    whisky_number = int(input("위스키 번호 : "))
    if 1 <= whisky_number <= len(Whisky_list):
        whisky_remove = Whisky_list.pop(whisky_number-1)
        with open("Whisky_data.json", "w", encoding="utf-8") as f:
            json.dump(Whisky_list, f, ensure_ascii=False, indent=2)
            print(f"'{whisky_remove['위스키']}' 위스키가 삭제되었습니다.")
    else:
        print("존재하지 않는 위스키 번호입니다.")


def edit():
    Whisky_list = select_list()
    if not Whisky_list:
        print("등록된 위스키가 없습니다.")
        return
    whisky_number = int(input("위스키 번호 : "))
    if 1 <= whisky_number <= len(Whisky_list):
        old_whisky = Whisky_list[whisky_number-1]
        print(f"'{old_whisky['위스키']}' 수정")
        whisky_name = input("Whisky : ")
        whisky_year = input("Whisky year : ")
        price = input("price : ")
        Whisky_data = Whisky(whisky_name, whisky_year, price)
        Whisky_dict = Whisky_data.to_dict()
        Whisky_list[whisky_number-1] = Whisky_dict
        with open("Whisky_data.json", "w", encoding="utf-8") as f:
            json.dump(Whisky_list, f, ensure_ascii=False, indent=2)
            print(f"'{old_whisky['위스키']}' 위스키가 수정되었습니다.")
    else:
        print("존재하지 않는 위스키 번호입니다.")


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