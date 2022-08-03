import socket
import sys
import traceback
from io import BytesIO

import keyboard
from pymycobot import MyCobot
import vcupycobot
import time

speed = 100
command_delay = 2 #seconds
command_history = []
ip = "192.168.0.11"
port = 80
sock = socket.socket()

def process_data(data):
    global speed

    if data:
        # Convert data to commands and sends commands to cobot
        command = data[0:3]
        joint_id = -1
        angles = 0

        if command == b"000":
            speed = int(data[3:], 2)
            print("Changed the Movement Speed to", speed)
        elif command == b"001":
            joint_id = int(data[3:6], 2)
            angles = int(data[7:], 2)

            sign_bit = int(data[6])
            if sign_bit == 1:
                angles = -angles

            print(f"Moving Joint {joint_id} to angle {angles}")
            mc.send_angle(joint_id, angles, speed)
            time.sleep(command_delay)
        elif command == b"010":
            angles = data[3:]
            angle_data = []

            while not len(angles) == 0:
                angle = angles[0:9]
                dec_val = int(angle[1:], 2)

                sign_bit = int(angle[0])
                if sign_bit == 1:
                    dec_val = -dec_val

                angle_data.append(dec_val)
                angles = angles[9:]

            print(f"Moving joints to to angles {angle_data}")
            mc.send_angles(angle_data, speed)
            time.sleep(command_delay)

### CODE ###

mc = MyCobot("COM3", 115)
#vcupycobot.check_cobot_connection(mc)
vcupycobot.move_to_origin(mc, 100)
time.sleep(2)

# Choose between TCP or UDP packets
while True:
    print("Select Your Communication Type:\n1) TCP\n2) UDP\n")
    ans = input("Communication Type: ")

    if ans == "1":
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        break
    elif ans == "2":
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        break
    else:
        print("Invalid Option. Please Try Again.")

# Bind the socket to the port
server_address = (ip, port)
print(f'Starting on {server_address} port {port}')
try:
    sock.bind(server_address)
except OSError:
    print("The server could not start with the inputted IP address. Check your computer's network connection.")
    traceback.print_exc()
    sys.exit()

# If the socket is a TCP socket...
if sock.type == socket.SOCK_STREAM:
    # Listen for incoming connections
    sock.listen(1)

while True:
    if sock.type == socket.SOCK_STREAM:
        # Wait for a connection
        print('Waiting for a connection...')
        (connection, client_address) = sock.accept()
        print('Connection from', client_address, "\n")

    try:
        # Receive the data, decodes it, and send the corresponding command to the cobot
        with BytesIO() as buffer:

            while True:

                resp = b""

                try:
                    if sock.type == socket.SOCK_STREAM:
                        resp = connection.recv(100)  # Read messages from connected client
                    elif sock.type == socket.SOCK_DGRAM:
                        resp = sock.recv(100)
                except ConnectionResetError:
                    break
                else:
                    buffer.write(resp)  # Write to the BytesIO object
                    buffer.seek(0)      # Set the file pointer to the SoF
                    start_index = 0     # Count the number of characters processed

                    data = buffer.readlines().pop()
                    data = data[:-1]

                    for line in buffer:
                        start_index += len(line)

                    process_data(data)

                    if start_index:
                        buffer.seek(start_index)
                        remaining = buffer.read()
                        buffer.truncate(0)
                        buffer.seek(0)
                        buffer.write(remaining)
                    else:
                        buffer.seek(0, 2)

                    if keyboard.is_pressed("enter"):
                        break

    finally:
        # Clean up the connection
        connection.close()

