import threading
import  time
for i in range(10):
    print("kh")
    time.sleep(0.1)
def f01():
    for i in range(10):
        print("Hello")
        time.sleep(0.1)
def f02():
    for i in range(10):
        print("World")
        time.sleep(0.1)
t1 = threading.Thread(target=f01).start()
t2 = threading.Thread(target=f02).start()
