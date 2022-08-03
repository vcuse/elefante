import socket
import sys
import traceback

#import keyboard

#server_ip = "192.168.73.48"
server_ip = "192.168.0.11"
port = 80

menu_text = "Select From the Options Below to Send Commands to the Cobot.\n" \
                    "1) Set the Cobot's Command Speed\n" \
                    "2) Send an Angle to a Joint on the Cobot\n" \
                    "3) Send Angles to all Joints on the Cobot\n" \
                    "4) Send a Coordinate to a Joint on the Cobot\n" \
                    "5) Send Coordinates to all Joints on the Cobot\n"

print("Welcome to the Cobot Command Server Client!\n Attempting to connect to the server now...")
try:
    # Change the aocket type below to socket.SOCK_DGRAM for UDP packets
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        print("\tConnected!\n")
        out_command = ""

        while True:
            print(menu_text)
            ans = input("Enter the Number Associated with the Command: ")

            try:
                ans = int(ans)-1

                if int(ans) == 0:
                    out_command += "000"

                    while True:
                        ans = input("\tEnter the Cobot's new movement speed (0 - 100): ")

                        if ans.isnumeric():
                            ans = int(ans)

                            if 0 <= ans <= 100:
                                bin_out = bin(ans).replace("0b", "")

                                while not len(bin_out) == 8:
                                    bin_out = "0" + bin_out

                                out_command += bin_out + "\n"
                                break
                            else:
                                print("\tPlease enter an integer from 0 to 100.")
                        else:
                            print("\tPlease enter an integer from 0 to 100.")

                    s.sendall(out_command.encode('utf-8'))
                elif int(ans) == 1:
                    out_command += "001"

                    while True:
                        ans = input("\tEnter the ID number of the joint you would like to move (1 - 6): ")

                        if ans.isnumeric():
                            ans = int(ans)

                            if 1 <= ans <= 6:
                                bin_out = bin(ans).replace("0b", "")

                                while not len(bin_out) == 3:
                                    bin_out = "0" + bin_out

                                out_command += bin_out
                                break
                            else:
                                print("\tPlease enter an integer from 1 to 6.")
                        else:
                            print("\tPlease enter an integer from 1 to 6.")

                    while True:
                        ans = input("\tEnter the new angle of the joint (-180 - 180): ")

                        if ans[0] == "-":
                            ans_check = ans[1:]
                        else:
                            ans_check = ans

                        if ans_check.isnumeric():
                            ans = int(ans)

                            if -180 <= ans < 0:
                                out_command += "1"
                                bin_out = bin(abs(ans)).replace("0b", "")

                                while not len(bin_out) == 8:
                                    bin_out = "0" + bin_out

                                out_command += bin_out + "\n"
                                break
                            elif 0 <= ans <= 180:
                                out_command += "0"
                                bin_out = bin(ans).replace("0b", "")

                                while not len(bin_out) == 8:
                                    bin_out = "0" + bin_out

                                out_command += bin_out + "\n"
                                break
                            else:
                                print("\tPlease enter a number from -180 to 180.")
                        else:
                            print("\tPlease enter a number from -180 to 180.")

                    s.sendall(out_command.encode('utf-8'))

                elif int(ans) == 2:
                    out_command += "010"
                    bin_angles = []

                    for i in range(6):
                        while True:
                            ans = input(f"\tEnter the new angle of Joint {i+1} (-180 - 180): ")
                            bin_num = ""

                            if ans[0] == "-":
                                ans_check = ans[1:]
                            else:
                                ans_check = ans

                            if ans_check.isnumeric():
                                ans = int(ans)
                                if -180 <= ans < 0:
                                    bin_num += "1"
                                    bin_out = bin(abs(ans)).replace("0b", "")

                                    while not len(bin_out) == 8:
                                        bin_out = "0" + bin_out

                                    bin_num = bin_num + bin_out
                                    break
                                elif 0 <= ans <= 180:
                                    bin_num += "0"
                                    bin_out = bin(ans).replace("0b", "")

                                    while not len(bin_out) == 8:
                                        bin_out = "0" + bin_out

                                    bin_num = bin_num + bin_out
                                    break
                                else:
                                    print("\tPlease enter a number from -180 to 180.")
                            else:
                                print("\tPlease enter a number from -180 to 180.")

                        bin_angles.append(bin_num)

                    for angle in bin_angles:
                        out_command += angle

                    out_command += "\n"
                    s.sendall(out_command.encode('utf-8'))
                else:
                    print("That command is currently under construction! Please try again.")

            except Exception as err0:
                print("Invalid Input. Please Try Again.")

except TimeoutError as err:
    print("Could Not Connect to the server. Connection Attempt Timeout. [WinError 10060]")
except Exception as err:
    traceback.print_exc()

