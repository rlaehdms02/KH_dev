from view.book_view import print_menu, scan_user_menu, procese

print("======도서 관리 프로그램======")

while True:
    print_menu()
    x = scan_user_menu()
    result = procese(x)
    if result == True: break
