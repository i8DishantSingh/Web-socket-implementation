import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 3000))

while True:
    
    message = input("You: ")
    client_socket.send(message.encode())
    resposne = client_socket.recv(1024)
    print("Server: ", resposne)

    