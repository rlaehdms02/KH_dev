def func02():
    print("-----dict-----")
    person = {"name" : "hong", "age" : 18, "blood": "A"}
    person["age"] += 1
    print(person)
    print(person["name"])
    print(person["age"])
    print(person["blood"])
    #print(person["MBTI"])
    print(person.get("mbti", "음성"))
    print("hong" )

def func02_1():
    x = {
        "board01": {"title":"~~", "content":"~~~~~", "writer" : "1234"} ,
        "p2": {"name":"영희", "age":21},
        "p3": {"name":"미영", "age":30}
    }
    print(x)

def func03():
    print("-----set-----")
    x = {10, 20, 30}
    y = {20, 30, 40}
    print(x & y)


def func04():
    x = 10, 20, 30
    print(x)



func04()