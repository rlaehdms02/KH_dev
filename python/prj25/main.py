import csv

def f01() -> None:
    with open("data.csv", "w", encoding="utf-8", newline='' ) as f:
        writer = csv.writer(f)
        writer.writerows([
            ["name", "age", "city"],
            ["홍길동", 20, "서울"],
            ["김철수", 22, "부산"]
        ])
def f02() -> None:
    with open("data.csv", "r", encoding="utf-8", newline='' ) as f:
        data = csv.reader(f)
        for row in data:
            print(row)

#dict 기반 (write)
def f03() -> None:
    data = [
        {"name":"홍길동", "age":20, "city":"서울"},
        {"name":"김철수", "age":22, "city":"부산"},
    ]
    with open("data.csv", "w", encoding="utf-8", newline='' ) as f:
        filenames = ["name", "age", "city"]
        writer = csv.DictWriter(f, fieldnames=filenames)
        writer.writeheader()
        writer.writerows(data)


#dict 기반 (read)
def f04() -> None:
   with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


f03()