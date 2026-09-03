def f01():
    print("fo1 called")
    f02()
    print("fo1 finished")
def f02():
    print("fo2 called")
    f03()
    print("fo2 finished")
def f03():
    print("fo3called")
    print("fo3 finished")
f01()