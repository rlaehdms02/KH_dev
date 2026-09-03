#파일 읽기
import csv

with open("loans.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    data = list(csv_reader)

#총 대출 건수 및 평균 대출일수
total = 0
cnt = 0
for row in data:
    total += int(row["대출일수"])
    cnt += 1

#분야별 대출 건수 내림차순
field = {}
for row in data:
    x =  row["분야"]
    field[x] = field.get(x, 0) + 1

print(field)

#대출자 유형별

category = {}
for row in data:
    y = row["대출자유형"]
    category[y] = category.get(y, 0) + 1
print(category)

#인기 분야

bast_dosu = ""
max_value = -1
for k, v in field.items():
    if v > max_value:
        max_value = v
        bast_dosu = k
print(bast_dosu, max_value)

#베스트 카테고리

bast_category = {}
max_category = -1
book = ""
for row in data:
    x = row["도서명"]
    bast_category[x] = bast_category.get(x, 0) + 1
    if bast_category[x] > max_category:
        max_category = bast_category[x]
        book = x
print(book, max_category)

#월별 매출
sales_by_month = {}

for row in data:
    k = row["대출일"][0:7]
    sales_by_month[k] = sales_by_month.get(k, 0) + 1
print(sales_by_month)


#리포트 파일 저장
with open("report02.txt", "w", encoding="utf-8") as f:
    f.write("=== 한빛도서관 대출 리포트 (2025.03 ~ 05) ===\n\n")
    f.write(f"[총 대출 건수] {cnt}건\n")
    f.write(f"[평균 대출일수] {total/cnt:.1f}일\n\n")
    f.write("[분야별 대출 건수]\n")
    sorted_field = sorted(field.items(), key=lambda x: x[1], reverse=True)
    for k,v in sorted_field:
        f.write(f"{k} : {v}건\n")
    sorted_category = sorted(category.items(), key=lambda x: x[1], reverse=True)
    f.write("\n[대출자 유형별]\n\n")
    for k, v in sorted_category:
        f.write(f"{k} : {v}건\n")
    f.write("\n[월별 대출 건수]\n")
    for m, s in sales_by_month.items():
        f.write(f"{m} : {s}건\n")
    f.write("\n[분석 결과]\n")
    f.write(f"최다 대출 도서 : {book} ({max_category}건)\n")
    f.write(f"인기 분야 1위 : {bast_dosu} ({max_value}건)\n")