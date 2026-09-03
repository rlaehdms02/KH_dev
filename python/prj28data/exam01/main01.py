#파일 읽기
import csv

with open("sales.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    data = list(csv_reader)

#전체 매출

total = 0
for row in data:
    total += int(row["단가"]) * int(row["수량"])

#메뉴별 판매 금액
qty_by_menu = {}
for row in data:
    x =  row["메뉴"]
    y = row["수량"]
    z = row["단가"]
    qty_by_menu[x] = qty_by_menu.get(x, 0) + int(y)

#카테고리별 매출
c_menu = {}
for row in data:
    x =  row["카테고리"]
    y = row["수량"]
    z = row["단가"]
    c_menu[x] = c_menu.get(x, 0) + int(y) * int(z)

#베스트 메뉴

bast_menu = ""
max_value = -1
for k, v in qty_by_menu.items():
    if v > max_value:
        max_value = v
        bast_menu = k

#베스트 카테고리
bast_category = ""
max_category = -1
for k, v in c_menu.items():
    if v > max_category:
        max_category = v
        bast_category = k

#월별 매출
sales_by_month = {}
for row in data:
    k = row["날짜"][0:7]
    result = int(row["단가"]) * int(row["수량"])
    sales_by_month[k] = sales_by_month.get(k, 0) + result
print(sales_by_month)


#리포트 파일 저장
with open("report01.txt", "w", encoding="utf-8") as f:
    f.write("=== 파이빈 카페 매출 리포트 (2025.01 ~ 03) ===\n\n")
    f.write(f"[전체 매출] {total:,}원\n\n")
    f.write("[메뉴별 판매금액]\n")
    sorted_qty = sorted(qty_by_menu.items(), key=lambda x: x[1], reverse=True)
    for k,v in sorted_qty:
        f.write(f"{k} : {v}잔\n")
    f.write("\n[카테고리별 판매금액]\n")
    sorted_c_menu = sorted(c_menu.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_c_menu:
        f.write(f"{k} : {v:,}원\n")
    f.write("\n[월별 매출]\n")
    for m, s in sales_by_month.items():
        f.write(f"{m} : {s:,}원\n")
    f.write("\n[분석 결과]\n")
    f.write(f"가장 많이 팔린 메뉴 : {bast_menu} ({max_value}잔)\n")
    f.write(f"매출 1위 카테고리 : {bast_category} ({max_category:,}원)\n")