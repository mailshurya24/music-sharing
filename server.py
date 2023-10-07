import socket
from threading import Thread

SERVER = None
IP_ADDR = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 4096

clients = {}

def acceptConnections():
    global SERVER, clients

    while True:
        client, addr = SERVER.accept()
        print(client,addr)

def setup():
    global SERVER, IP_ADDR, PORT

    print("\t\t\t\t\tIP MESSENGER")

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDR, PORT))

    SERVER.listen(100)

    print ("\n\t\t\t\t\tSERVER WAITING FOR CONNECTIONS")

    acceptConnections()

thread1 = Thread(target = setup)
thread1.start()