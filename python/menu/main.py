from random import random, randint

kr_food_menu = ["순대국", "뼈해장국", "비빔밥", "김치찜", "국수", "곰탕","부대찌개", "닭도리탕", "감자탕", "김치찌개", "백반", "한식뷔폐", "제육", "갈비탕", "샤브샤브", "설렁탕", "분식", "냉면"]
jp_food_menu = ["돈카츠", "텐동", "라멘", "우동", "메밀소바", "덮밥", "카레","오므라이스", "규동"]
ch_food_menu = ["중식", "마라탕", "훠궈", "볶음밥", "짜장면", "짬뽕", "탕수육"]
us_food_menu = ["햄버거", "피자", "리조또", "샌드위치", "샐러드", "타코", "부리또", "그라탕", "파스타", "라자냐"]
while True:
    food = randint(1, 4)
    match food:
        case 1:
            food = "한식"
        case 2:
            food = "일식"
        case 3:
            food = "중식"
        case 4:
            food = "양식"
    if food == "한식":
        print(food)
        print(kr_food_menu[randint(0, len(kr_food_menu) - 1)])
    elif food == "일식":
        print(food)
        print(jp_food_menu[randint(0, len(jp_food_menu) - 1)])
    elif food == "중식":
        print(food)
        print(ch_food_menu[randint(0, len(ch_food_menu) - 1)])
    elif food == "양식":
        print(food)
        print(us_food_menu[randint(0, len(us_food_menu) - 1)])
    print("재추천 : 1, 추천끝 : 0")
    retry  = int(input())
    if retry == 0:
        break
    else:
        continue