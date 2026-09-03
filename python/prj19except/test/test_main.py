from member import join

try:
    join()
except Exception as e:
    print("회원가입 하다가 예외 발생", e)