import socket 

#server address
serverIP = socket.gethostbyname(socket.gethostname())
serverPORT = 5050

#creating client socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connecting client to server 
client.connect((serverIP,serverPORT))
print(f"[*] connected to server {serverIP}:{serverPORT}")

#sending message to server
while True:
    msg = input("[*] Enter your message: \n")
    client.send(msg.encode())
    if client.recv(1024).decode() == "close":
        client.close()
        break 