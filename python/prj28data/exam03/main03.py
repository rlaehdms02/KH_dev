#파일 읽기
import csv

with open("weather.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    data = list(csv_reader)
    total_cnt = len(data)

#전체 관측 및 비 온 날
cnt = 0
total = 0
rain = 0
for row in data:
    x = row["강수량"]
    if x != "0":
        cnt  += 1
rain = cnt / total_cnt * 100
#print(f"{rain:.1f}%")


#평균 기온 계산
city_temp = {}

for row in data:
    city = row["도시"]
    temp = float(row["최고기온"])
    if city not in city_temp:
        city_temp[city] = [0.0, 0]

    city_temp[city][0] += temp
    city_temp[city][1] += 1

city_avg = {}
for city, (total, count) in city_temp.items():
    city_avg[city] = total / count

sorted_city_avg = sorted(city_avg.items(), key=lambda x: x[1], reverse=True)


max_city = -1
bast_city = ""
max_c = 0

for row in data:
    max_c =  int(row["최고기온"])
    y = row["날짜"]
    z = row["도시"]
    if max_c > max_city:
        max_city = max_c
        max_date = y
        bast_city = z

ilgyocha_city = -1
ilgyocha_bast_city = ""
ilgyocha = 0

for row in data:
    ilgyocha_max = int(row["최고기온"])
    ilgyocha_min = int(row["최저기온"])
    y = row["날짜"]
    z = row["도시"]
    if ilgyocha_max-ilgyocha_min > ilgyocha_city:
        ilgyocha_city = ilgyocha_max-ilgyocha_min
        ilgyocha = y
        ilgyocha_bast_city = z

#리포트 파일 저장
with open("report03.txt", "w", encoding="utf-8") as f:
    f.write("=== 여름 날씨 분석 리포트 (2025.06 ~ 08) ===\n\n")
    f.write(f"[전체 관측] {total_cnt}건\n")
    f.write(f"[비 온 날] {cnt}건 ({rain:.1f}%)\n")
    f.write("\n[도시별 평균 최고기온]\n")
    for k,v in sorted_city_avg:
        f.write(f"{k} : {v:.1f}℃\n")
    f.write("\n[분석 결과]\n")
    f.write(f"가장 더웠던 날 : {max_date} : {bast_city} ({max_city}℃)\n")
    f.write(f"일교차가 가장 큰 날 : {ilgyocha} {ilgyocha_bast_city} ({ilgyocha_city}℃)\n")