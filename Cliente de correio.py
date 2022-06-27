from socket import *
import time, base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

MAILSERVER = "smtp.mailtrap.io"
PORT = 2525

MAIL = (MAILSERVER, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((MAILSERVER, PORT))

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')


heloCommand = 'HELO <thundercraft124@gmail.com>\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')
  
# Send EMAIL FROM command and print server response.

emailFrom = "EMAIL FROM:<thundercraft124@gmail.com>"
clientSocket.send(emailFrom.encode())

recv2 = clientSocket.recv(1024).decode()
print(recv2)
  
# Send RCPT TO command and print server response.

recpTo = "RCPT TO:<lukasjp446@gmail.com>\r\n"
clientSocket.send(recpTo.encode())

recv3 = clientSocket.recv(1024).decode()
print(recv3)

  
# Send DATA command and print server response.

data = "DATA\r\n"
clientSocket.send(data.encode())

recv4 = clientSocket.recv(1024).decode()
print(recv4)


# Send message data.

clientSocket.send(msg.encode())

# Message ends with a single period.

clientSocket.send(endmsg.encode())

recv5 = clientSocket.recv(1024).decode()
print(recv5)


# Send QUIT command and get server response.

QUIT = "QUIT\r\n"
clientSocket.send(QUIT.encode())

recv6 = clientSocket.recv(1024)
print(recv6.decode())
