import socket

HOST = '192.168.206.36' 
PORT = 60938

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server")

off = False
while not off:
    data_client = input("You: ")
    client.send(data_client.encode('utf-8'))
    if data_client == 'quit':
        print('Client quit')
        off = True
    else:
        msg = client.recv(1024).decode('utf-8')
        if msg == 'quit':
            print('Server quit')
            off = True
        else:
            print(f"Server: {msg}")

client.close()
print("Connection closed")