from book_manager import scan_user_input, print_menu, process

print("===== 도서 관리 프로그램 =====")

while True:
    try:
        print_menu()
        num = scan_user_input()
        is_running = process(num)
        if not is_running: break
    except Exception as e:
        print(e)

