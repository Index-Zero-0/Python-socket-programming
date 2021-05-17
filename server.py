import socket
from threading import Thread

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server is running on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Got a new connection from {addr[0]}")

conn.send("You connected successfully to server".encode('utf-8'))

def recievingMsg(connection):
    while True:
        msg = connection.recv(1024).decode('utf-8')
        if msg:
            print(msg)


recievThread = Thread(target=recievingMsg,args=(conn,))
recievThread.start()

while True:
    msg = "Server@ "
    msg += input("")
    conn.send(msg.encode('utf-8'))
