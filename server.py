import socket

HOST = '0.0.0.0'  
PORT = 60938

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is running and listening for connections...")
conn, addr = server.accept()
print(f"Connected to {addr}")

off = False
while not off:
    data_server = conn.recv(1024).decode('utf-8')
    if data_server == 'quit':
        print('Client quit')
        off = True
    else:
        print(f"Client: {data_server}")
        data_server = input("You: ")
        conn.send(data_server.encode('utf-8'))
        if data_server == 'quit':
            print('Server quit')
            off = True
        

conn.close()
print("Connection closed")