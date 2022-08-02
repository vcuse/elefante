import socket
import keyboard
from pymycobot import MyCobot
import vcupycobot
import time

mc = MyCobot("COM3", 115)
vcupycobot.check_cobot_connection(mc)
speed = 100
command_delay = 2 #seconds

ip = "192.168.73.48"
port = 80

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ("192.168.73.48", 80)
print(f'starting up on {server_address} port {port}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    (connection, client_address) = sock.accept()

    try:
        print('connection from', client_address)

        # Receive the data and send it to the cobot
        while True:
            data = connection.recv(57)

            if data:
                print('received "%s"' % data)

                # Convert data to commands and sends commands to cobot
                command = data[0:4]
                joint_id = -1
                angles = 0

                if command == b"000":
                    speed = int(data[4:], 2)
                    print("Changed the Movement Speed to", speed)
                    break
                elif command == b"001":
                    joint_id = int(data[3:6], 2)
                    angles = int(data[7:], 2)

                    sign_bit = int(data[6])
                    if sign_bit:
                        angles = -angles

                    print(f"Moving Joint {joint_id} to angle {angles}")
                    mc.send_angle(joint_id, angles, speed)
                    time.sleep(command_delay)
                    break
                elif command == b"010":
                    angles = data[3:]
                    angle_data = []

                    while not len(angles) == 0:
                        angle = angles[0:9]
                        dec_val = int(angle[1:], 2)

                        sign_bit = int(angle[0])
                        if sign_bit:
                            dec_val = -dec_val

                        angle_data.append(dec_val)
                        angles = angles[9:]

                    print(f"Moving joints to to angles {angle_data}")
                    mc.send_angles(angle_data, speed)
                    time.sleep(command_delay)
                    break
                elif command == b"011":
                    #send_coord()
                    break
                elif command == b"100":
                    #send_coords()
                    break
                # Add more command checks to add functionality
                else:
                    break

            if keyboard.is_pressed("enter"):
                connection.close()
                break

    finally:
        # Clean up the connection
        connection.close()