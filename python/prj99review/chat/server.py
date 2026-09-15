import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('192.168.40.91', 9876))
server_socket.listen()
print("나 서버소켓인데,,, 연결 대기중이야 ...")

conn, addr = server_socket.accept()
print("접속한 addr : ", addr)


def receive():
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("not data : ", data)
                print("상대방 나감")
                break
            print("[상대방]", data.decode())
        except Exception as e:
            print("예외발생 !!!", e)
            break


threading.Thread(target=receive, daemon=True).start()

while True:
    # 발신
    msg = input("보낼 메세지 : ")
    conn.send(msg.encode())
