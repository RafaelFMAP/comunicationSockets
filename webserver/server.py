import socket

BYTES_TO_RECEIVE = 64
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR =  (HOST, PORT)
FORMAT = "UTF-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New connection: {addr} connected to the server")

    connected = True
    while connected:
        lengthOfMessage = conn.recv(BYTES_TO_RECEIVE).decode(FORMAT)
        if lengthOfMessage:
            lengthOfMessage = int(lengthOfMessage)

            fileToOpen = conn.recv(lengthOfMessage).decode(FORMAT)
            if fileToOpen:
                print("File on Archive")
            else:
                print("404 Not Found")

    server.close()

def start_connection():
    server.listen()
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

start_connection()