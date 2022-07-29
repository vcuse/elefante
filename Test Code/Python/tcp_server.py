import socket
import sys
import keyboard

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ("192.168.73.48", 80)
print(sys.stderr, f'starting up on {server_address} port 80')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    (connection, client_address) = sock.accept()

    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)

            if data:
                #print(sys.stderr, 'sending data back to the client')
                #connection.sendall(data)

                print('received:', data)

            if keyboard.is_pressed("enter"):
                connection.close()
                break


    finally:
        # Clean up the connection
        connection.close()