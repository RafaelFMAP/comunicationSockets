from socket import *
import time

for pings in range(10):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    addr = ("127.0.0.1",12000)

    message = "Ping"
    message = message.encode()

    startTime = time.time()
    clientSocket.sendto(message, addr)

    try:
        data, server = clientSocket.recvfrom(1024)
        endTime = time.time()
        timeElapsed = endTime - startTime
        print(f'{data}, {pings}, {timeElapsed}')
    except:
        print("Package Lost")