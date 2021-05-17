import socket
from threading import Thread

SERVER_IP = socket.gethostname()
SERVER_PORT = 1234
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))


def receivingMsg(conn):
    while True:
        msg = conn.recv(128).decode("utf-8")
        if msg:
            print(msg)


recievThread = Thread(target=receivingMsg, args=(client,))
recievThread.daemon = True
recievThread.start()

while True:
    msg = "Client@ "
    msg += input("")
    client.send(msg.encode('utf-8'))
