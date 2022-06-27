from ctypes.wintypes import BYTE
import socket

BYTES_TO_RECEIVE = 64
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR =  (HOST, PORT)
FORMAT = "UTF-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message_proxy(msg):
    message = msg.encode(FORMAT)
    messageLength = len(message)
    sendLenght = str(messageLength).encode(FORMAT)
    sendLenght += b' ' * (BYTES_TO_RECEIVE - len(sendLenght))
    client.send(sendLenght)
    client.send(message)

send_message_proxy("homepage.html")

messagelen = client.recv(BYTES_TO_RECEIVE)
message = client.recv(messagelen).decode()
print(message)